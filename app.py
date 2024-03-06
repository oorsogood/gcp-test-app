# app.py
from flask import Flask

# Create a Flask application instance
app = Flask(__name__)


# Define a route for the root URL ("/") that returns an HTML page with a styled greeting
@app.route("/")
def hello():
    return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>My Personal Blog</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f0f0f0;
                }
                header {
                    background-color: #333;
                    color: #fff;
                    padding: 20px;
                    text-align: center;
                }
                nav {
                    background-color: #444;
                    padding: 10px;
                    text-align: center;
                }
                nav a {
                    color: #fff;
                    text-decoration: none;
                    margin: 0 10px;
                }
                nav a:hover {
                    text-decoration: underline;
                }
                .container {
                    max-width: 800px;
                    margin: 20px auto;
                    padding: 0 20px;
                }
                .post {
                    background-color: #fff;
                    padding: 20px;
                    margin-bottom: 20px;
                }
                .post h2 {
                    margin-top: 0;
                }
                .post p {
                    line-height: 1.6;
                }
            </style>
        </head>
        <body>
            <header>
                <h1>My Personal Blog</h1>
            </header>
            <nav>
                <a href="#">Home</a>
                <a href="#">About</a>
                <a href="#">Contact</a>
            </nav>
            <div class="container">
                <div class="post">
                    <h2>My First Blog Post</h2>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam vehicula metus ut nulla vestibulum, nec aliquet felis eleifend. Nam condimentum metus id ex consequat, nec malesuada nunc ultrices.</p>
                </div>
                <div class="post">
                    <h2>My Second Blog Post</h2>
                    
                    <p>Etiam a nisl at risus viverra lacinia. Nulla facilisi. In hac habitasse platea dictumst. Suspendisse potenti. Aenean vitae ligula nunc. In nec ipsum et nulla vestibulum accumsan. Sed vel ipsum ut magna vehicula pretium nec non orci.</p>
                </div>
                <!-- Add more posts here -->
            </div>
        </body>
        </html>
    """


# Start the Flask web server if this script is executed directly
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
