# Flask Blog App

A simple blog application built with Flask and SQLAlchemy that allows users to create, read, edit, and delete blog posts.

## Features

- Create new blog posts with title, content, and author
- View all blog posts ordered by date
- Edit existing posts
- Delete posts
- SQLite database for data persistence

## Requirements

- Python 3.12
- Flask
- Flask-SQLAlchemy

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Flask-Blog-App
```

2. Install dependencies using Pipenv:
```bash
pipenv install
```

3. Activate the virtual environment:
```bash
pipenv shell
```

## Usage

1. Run the application:
```bash
python app.py
```

2. Open your browser and navigate to `http://127.0.0.1:5000`

## Routes

- `/` - Home page
- `/posts` - View all posts (GET) or create a new post (POST)
- `/posts/new` - Form to create a new post
- `/posts/edit/<id>` - Edit an existing post
- `/posts/delete/<id>` - Delete a post

## Database

The application uses SQLite with the following schema:

**BlogPost Model:**
- `id` - Primary key
- `title` - Post title (max 100 characters)
- `content` - Post content (text)
- `author` - Author name (defaults to "Unknown Author")
- `date_posted` - Timestamp of post creation

## Project Structure

```
Flask-Blog-App/
├── app.py              # Main application file
├── instance/
│   └── posts.db        # SQLite database
├── static/
│   ├── css/
│   │   └── main.css    # Stylesheets
│   └── js/
│       └── main.js     # JavaScript files
├── templates/
│   ├── base.html       # Base template
│   ├── index.html      # Home page
│   ├── posts.html      # All posts view
│   ├── new_post.html   # Create post form
│   └── edit.html       # Edit post form
├── Pipfile             # Dependencies
└── Pipfile.lock        # Locked dependencies
```

## License

This project is open source and available for educational purposes.
