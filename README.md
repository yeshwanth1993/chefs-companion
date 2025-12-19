# Chefs Companion

A Flask-based web application for discovering, managing, and rating recipes. Browse, add, and rate recipes with comments and image uploads.

## Features

*   **Recipe Browsing & Management**: View, add, and see detailed pages for recipes.
*   **User Ratings**: Rate recipes, leave comments (with profanity filtering and sentiment analysis), and upload images.
*   **Discover**: Find popular recipes based on user ratings.

## Technologies

*   **Backend**: Python (Flask)
*   **Frontend**: HTML/CSS (Jinja2)
*   **Libraries**: Pillow, better-profanity, TextBlob
*   **Deployment**: Docker, Google Cloud Build & Cloud Run

## Getting Started

### Prerequisites

*   Python 3.10+
*   Docker (optional)

### Local Setup

1.  **Clone the repo & install dependencies:**
    ```bash
    git clone https://github.com/your-username/chefs-companion.git
    cd chefs-companion
    pip install -r requirements.txt
    ```

2.  **Run the app:**
    ```bash
    python app.py
    ```
    View at `http://127.0.0.1:8080`.

### Docker

```bash
docker build -t chefs-companion .
docker run -p 8080:8080 chefs-companion
```