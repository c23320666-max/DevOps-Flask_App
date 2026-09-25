from flask import Flask

app = Flask(__name__)

# Homepage route
@app.route("/")
def home():
    return """
    <h1>Home Page</h1>
    <p>Welcome to the DevOps Flask App!</p>
    <nav>
        <a href="/about">About Us</a> | 
        <a href="/contact">Contact Us</a>
        
    </nav>
    """

# About page route
@app.route("/about")
def about():
    return """
    <h1>About Page</h1>
    <p>This is the about page for our application. </p>
    <a href="/">Back to Home</a>
    """

# Contact page route
@app.route("/contact")
def contact():
    return """
    <h1>Contact Page</h1>
    <p>Get in touch with us at: <a href="mailto:your.email@example.com">your.email@example.com</a></p>
    <a href="/">Back to Home</a>
    """

if __name__ == "__main__":
    app.run(debug=True)
