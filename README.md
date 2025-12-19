# Chef's Companion

## Project Description
Chef's Companion is a web application designed to help users manage recipes, track ingredients, and potentially rate dishes. It aims to be a helpful tool for home cooks and culinary enthusiasts.

## Features
- Recipe management (add, view, edit recipes)
- Ingredient tracking
- User authentication (planned/future)
- Recipe rating and review system

## Setup and Installation

To get Chef's Companion up and running on your local machine, follow these steps:

### Prerequisites
- Python 3.8+
- Docker (for containerized deployment)

### Local Development
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/chefs-companion.git
    cd chefs-companion
    ```

2.  **Create a virtual environment and activate it:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**
    ```bash
    export FLASK_APP=app.py
    flask run
    ```
    The application will be accessible at `http://127.0.0.1:5000`.

### Docker Deployment
1.  **Build the Docker image:**
    ```bash
    docker build -t chefs-companion .
    ```

2.  **Run the Docker container:**
    ```bash
    docker run -p 5000:5000 chefs-companion
    ```
    The application will be accessible at `http://localhost:5000`.

## Usage
Once the application is running, open your web browser and navigate to the provided address. You can then start adding and managing your recipes.

## Technologies Used
- Python
- Flask (Web Framework)
- HTML/CSS/JavaScript (Frontend)
- Docker (Containerization)

## Contributing
Contributions are welcome! Please feel free to fork the repository, make changes, and submit pull requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details (if applicable).