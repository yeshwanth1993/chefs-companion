from flask import Flask, jsonify, request

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
        'instructions': recipe_data['instructions']
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

if __name__ == '__main__':
    app.run(host='0.0.0.0')
