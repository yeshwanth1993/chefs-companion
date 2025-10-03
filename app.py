from flask import Flask, jsonify, request
from better_profanity import profanity

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

@app.route('/recipes/<string:recipe_name>/rate', methods=['POST'])
def rate_recipe(recipe_name):
    """Rates a recipe."""
    recipe = recipes_db.get(recipe_name)
    if not recipe:
        return jsonify({'error': f'Recipe with name "{recipe_name}" not found.'}), 404

    rating_data = request.get_json()
    if not rating_data or 'rating' not in rating_data:
        return jsonify({'error': 'Invalid rating data. Required fields: rating'}), 400

    rating = rating_data['rating']
    if not isinstance(rating, int) or not 1 <= rating <= 5:
        return jsonify({'error': 'Rating must be an integer between 1 and 5.'}), 400

    comment = rating_data.get('comment', '')
    sanitized_comment = profanity.censor(text)

    recipe['ratings'].append({
        'rating': rating,
        'comment': sanitized_comment
    })

    return jsonify({'message': f'Thank you for rating "{recipe_name}".'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')
