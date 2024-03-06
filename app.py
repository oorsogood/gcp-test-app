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
                }
                header {
                    background-color: #333;
                    color: #fff;
                    padding: 20px;
                    text-align: center;
                }
                nav {
                    background-color: #666;
                    padding: 10px;
                    text-align: center;
                }
                nav a {
                    color: #fff;
                    text-decoration: none;
                    margin: 0 10px;
                }
                main {
                    padding: 20px;
                }
                footer {
                    background-color: #333;
                    color: #fff;
                    text-align: center;
                    padding: 10px;
                    position: fixed;
                    bottom: 0;
                    width: 100%;
                }
            </style>
        </head>
        <body>
            <header>
                <h1>Welcome to My Personal Blog</h1>
            </header>
            <nav>
                <a href="#">Home</a>
                <a href="#">About</a>
                <a href="#">Contact</a>
            </nav>
            <main>
                <h2>Latest Posts</h2>
                <article>
                    <h3>Post Title 1</h3>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed tempus ligula vitae dolor dictum, sed dapibus massa lacinia. Donec eu arcu vel arcu elementum ultrices id a nisl. Duis id nunc sed velit bibendum suscipit. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Integer feugiat tincidunt metus, nec aliquam neque consectetur in. Vivamus pretium erat quis arcu feugiat, sed lobortis sapien consectetur.</p>
                </article>
                <article>
                    <h3>Post Title 2</h3>
                    <p>Integer nec libero sollicitudin, faucibus orci nec, volutpat urna. Suspendisse quis tortor tellus. Duis convallis elit vel dui consequat, nec auctor dui euismod. Vestibulum vitae tortor a metus laoreet ultricies eu vitae ipsum. Vivamus posuere vestibulum magna, vel ultrices nunc convallis ut. Sed eu nibh justo.</p>
                </article>
            </main>
            <footer>
                <p>&copy; 2024 My Personal Blog</p>
            </footer>
        </body>
        </html>
    """


# Start the Flask web server if this script is executed directly
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
