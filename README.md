# Chefs Companion

## Overview

Chefs Companion is a Flask-based web application designed to help users discover, manage, and rate recipes. It provides a platform to browse existing recipes, add new ones, view popular dishes, and leave ratings with comments and image uploads. Comments are sanitized for profanity, and sentiment analysis is performed on user feedback.

## Features

*   **Recipe Browsing**: View a list of available recipes.
*   **Individual Recipe Pages**: Detailed view for each recipe, including ingredients and instructions.
*   **Add New Recipes**: API endpoint to programmatically add new recipes to the collection.
*   **Popular Recipes**: Discover recipes based on average user ratings.
*   **Recipe Rating & Image Upload**: Rate recipes, add comments, and upload an image of your culinary creation.
    *   Comments are automatically censored for profanity.
    *   Sentiment analysis is performed on comments.
    *   Uploaded images are processed to create 256x256 thumbnails.

## Technologies Used

*   **Backend**: Python (Flask)
*   **Frontend**: HTML, CSS (via Jinja2 templates)
*   **Database**: In-memory Python dictionary (for demonstration purposes)
*   **Libraries**:
    *   `Pillow`: Image processing for thumbnails.
    *   `better-profanity`: Profanity filtering for comments.
    *   `TextBlob`: Sentiment analysis for comments.
*   **Containerization**: Docker
*   **CI/CD & Deployment**: Google Cloud Build, Google Cloud Run

## Getting Started

### Prerequisites

*   Python 3.10+
*   `pip` (Python package installer)
*   Docker (optional, for containerized development)
*   Google Cloud SDK (optional, for deployment to Google Cloud Run)

### Local Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/chefs-companion.git
    cd chefs-companion
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**
    ```bash
    python app.py
    ```
    The application will be accessible at `http://127.0.0.1:8080`.

### Docker Setup (Local)

1.  **Build the Docker image:**
    ```bash
    docker build -t chefs-companion .
    ```

2.  **Run the Docker container:**
    ```bash
    docker run -p 8080:8080 chefs-companion
    ```
    The application will be accessible at `http://localhost:8080`.

## API Endpoints

*   `GET /`: Home page.
*   `GET /recipe/<string:recipe_name>`: View a specific recipe page.
*   `GET /recipes`: Get all recipes.
*   `GET /recipes/popular`: Get recipes sorted by average rating.
*   `GET /recipes/<string:recipe_name>`: Get a specific recipe's JSON data.
*   `POST /recipes`: Add a new recipe. Requires JSON payload with `name`, `ingredients`, `instructions`.
*   `POST /recipes/<string:recipe_name>/rate`: Rate a recipe. Requires `multipart/form-data` with `rating` (1-5), optional `comment`, and `image` file.

## Deployment to Google Cloud Run

This project includes a `cloudbuild.yaml` configuration for automated deployment to Google Cloud Run via Google Cloud Build.

1.  **Enable Google Cloud APIs**: Ensure Cloud Build, Cloud Run, and Artifact Registry APIs are enabled in your GCP project.
2.  **Configure Artifact Registry**: Create a Docker repository in Google Artifact Registry (e.g., `us-central1-docker.pkg.dev/gcp-playground-boa/chefs-companion-repo`). Update `cloudbuild.yaml` with your project and repository details if they differ.
3.  **Submit the build**:
    ```bash
    gcloud builds submit --config cloudbuild.yaml .
    ```
    This command will build the Docker image, push it to Artifact Registry, and deploy it as a new revision to the `chefs-companion-service` in Google Cloud Run.

---
