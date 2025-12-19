# Chef's Companion

A simple and interactive Flask-based web application for managing and exploring a collection of recipes. This application allows users to view recipe details, add new recipes, and rate existing ones with comments and images.

## Features

*   **Recipe Management:** View a list of pre-loaded recipes and add new ones to the collection.
*   **Detailed Recipe View:** Each recipe has its own page with ingredients, instructions, and an image.
*   **Recipe Ratings:** Users can submit a rating (1-5 stars) for any recipe.
*   **Comments with Sentiment Analysis:** Leave comments along with ratings, which are analyzed for sentiment polarity and subjectivity.
*   **Image Uploads:** Users can upload an image with their rating, and the application will automatically generate and save a thumbnail.
*   **Profanity Filter:** All user-submitted comments are sanitized to remove inappropriate language.
*   **Popular Recipes:** An API endpoint is available to retrieve recipes sorted by their average rating.

## Technologies Used

*   **Backend:** Python, Flask
*   **Image Processing:** Pillow
*   **Text Analysis:**
    *   `better-profanity` for filtering profanity.
    *   `TextBlob` for sentiment analysis.

## Project Structure

```
├── app.py                # Main Flask application logic
├── Dockerfile            # Container configuration for deployment
├── cloudbuild.yaml       # Google Cloud Build configuration
├── requirements.txt      # Python dependencies
├── templates/
│   ├── index.html        # Home page template
│   └── recipe.html       # Recipe page template
└── uploads/
    └── recipe_ratings/   # Directory for storing uploaded rating images
```

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd chefs-companion
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

To start the local development server, run the following command:

```bash
python app.py
```

The application will be accessible at `http://0.0.0.0:8080`.

## API Endpoints

The application exposes the following RESTful API endpoints for interacting with the recipe data:

| Method | Endpoint                             | Description                                            |
|--------|--------------------------------------|--------------------------------------------------------|
| `GET`  | `/`                                  | Renders the home page.                                 |
| `GET`  | `/recipe/<string:recipe_name>`       | Renders the page for a specific recipe.                |
| `GET`  | `/recipes`                           | Retrieves a JSON list of all recipes.                  |
| `POST` | `/recipes`                           | Adds a new recipe to the collection.                   |
| `GET`  | `/recipes/<string:recipe_name>`      | Retrieves the details of a single recipe.              |
| `GET`  | `/recipes/popular`                   | Retrieves recipes sorted by their average rating.      |
| `POST` | `/recipes/<string:recipe_name>/rate` | Submits a rating, comment, and image for a recipe.     |
