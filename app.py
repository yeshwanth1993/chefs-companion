from flask import Flask, jsonify, request
from better_profanity import profanity
from textblob import TextBlob
import os 

# You may need to load the default wordlist once
profanity.load_censor_words() 

app = Flask(__name__)

# In-memory data store for recipes
recipes_db = {}

@app.route('/recipes', methods=['POST'])
def add_recipe():
    """Adds a new recipe to the cook book"""
    recipe_data = request.get_json()
    if not recipe_data or 'name' not in recipe_data or 'ingredients' not in recipe_data or 'instructions' not in recipe_data:
        return jsonify({'error': 'Invalid recipe data. Required fields: name, ingredients, instructions'}), 400
    
    recipe_name = recipe_data['name']
    if recipe_name in recipes_db:
        return jsonify({'error': f'Recipe with name "{recipe_name}" already exists.'}), 409
    
    recipes_db[recipe_name] = {
        'name': recipe_name,
        'ingredients': recipe_data['ingredients'],
        'instructions': recipe_data['instructions'],
        'ratings': []
    }
    
    return jsonify({'message': f'Recipe "{recipe_name}" added successfully.'}), 201

@app.route('/recipes/<string:recipe_name>', methods=['GET'])
def get_recipe(recipe_name):
    """Retrieves a recipe by name."""
    recipe = recipes_db.get(recipe_name)
    if recipe:
        return jsonify(recipe)
    else:
        return jsonify({'error': f'Recipe with name "{recipe_name}" not found.'}), 404

@app.route('/recipes', methods=['GET'])
def get_all_recipes():
    """Retrieves all recipes."""
    return jsonify(list(recipes_db.values()))

UPLOAD_FOLDER = 'uploads/recipe_ratings'
os.makedirs(UPLOAD_FOLDER, exist_ok=True) # Ensure the upload directory exists

@app.route('/recipes/<string:recipe_name>/rate', methods=['POST'])
def rate_recipe(recipe_name):
    """Rates a recipe and processes an uploaded image."""
    recipe = recipes_db.get(recipe_name)
    if not recipe:
        return jsonify({'error': f'Recipe "{recipe_name}" not found.'}), 404

    # 1. Get rating and comment from the form fields
    if 'rating' not in request.form:
        return jsonify({'error': 'Invalid data. Required field: rating'}), 400
    
    # 2. Get the uploaded image file
    if 'image' not in request.files:
        return jsonify({'error': 'Invalid data. Required file: image'}), 400

    # 3. Validate rating (it will be a string from the form)
    try:
        rating = int(request.form['rating'])
        if not 1 <= rating <= 5:
            raise ValueError
    except ValueError:
        return jsonify({'error': 'Rating must be an integer between 1 and 5.'}), 400

    image_file = request.files['image']
    comment = request.form.get('comment', '')

    # 4. Process the image with Pillow to create a thumbnail
    try:
        img = Image.open(image_file.stream)
        img.thumbnail((256, 256)) # Create a 256x256 thumbnail
        
        # 5. Save the thumbnail with a unique filename
        _, ext = os.path.splitext(image_file.filename)
        thumbnail_filename = f"{uuid.uuid4().hex}{ext}"
        thumbnail_path = os.path.join(UPLOAD_FOLDER, thumbnail_filename)
        img.save(thumbnail_path)
    except Exception as e:
        return jsonify({'error': f'Failed to process image: {e}'}), 500

    # Sanitize comment and get sentiment
    sanitized_comment = profanity.censor(comment)
    sentiment = TextBlob(sanitized_comment).sentiment

    # 6. Store the rating data, including the path to the thumbnail
    recipe['ratings'].append({
        'rating': rating,
        'comment': sanitized_comment,
        'thumbnail': thumbnail_path, # Store the path to the saved image
        'sentiment': {
            'polarity': sentiment.polarity,
            'subjectivity': sentiment.subjectivity
        }
    })

    return jsonify({'message': f'Thank you for rating "{recipe_name}".'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')
