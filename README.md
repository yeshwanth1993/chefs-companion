# Chef's Companion

A Flask-based web application for discovering, managing, and rating recipes.

## Features

*   **Recipe Discovery**: Browse a collection of recipes.
*   **Detailed Recipe View**: See ingredients, instructions, and user ratings for each recipe.
*   **Add New Recipes**: Contribute your own recipes to the collection.
*   **Rate and Comment**: Rate recipes on a scale of 1 to 5, leave comments, and upload images of your creations.
*   **Profanity Filtering and Sentiment Analysis**: Comments are checked for profanity and analyzed for sentiment.
*   **Popular Recipes**: Discover new recipes based on user ratings.

## Technologies Used

*   **Backend**: Python with Flask
*   **Frontend**: HTML and CSS with Jinja2 templating
*   **Libraries**:
    *   Pillow for image processing
    *   better-profanity for filtering profanity from comments
    *   TextBlob for sentiment analysis of comments

## Getting Started

### Prerequisites

*   Python 3.10 or higher
*   pip for installing Python packages

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/chefs-companion.git
    ```

2.  **Navigate to the project directory:**

    ```bash
    cd chefs-companion
    ```

3.  **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1.  **Run the Flask application:**

    ```bash
    python app.py
    ```

2.  **Open your web browser and navigate to:**

    ```
    http://127.0.0.1:8080
    ```

## How to Use - modified this line

*   **Home Page**: The home page displays a list of all available recipes.
*   **Recipe Details**: Click on a recipe to view its details, including ingredients, instructions, and user ratings.
*   **Add a Recipe**: Use the "Add Recipe" form to add a new recipe to the collection.
*   **Rate a Recipe**: On the recipe details page, you can rate the recipe from 1 to 5 stars, leave a comment, and upload an image.
-- added line 1
-- added line 2