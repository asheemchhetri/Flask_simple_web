from flask import Flask, render_template

# Creating an object for our web-application
app = Flask(__name__, template_folder="templates")

'''
Telling our web application what to display when a user lands on home page (i.e. / or /home) or also known as home URL
Execute the function called home()
Behavior: Run a HTML file to display to a user as soon they land on the home URL
Parameters: None
'''

@app.route("/")
@app.route("/home")
def home():
    return render_template("html/home.html")

'''
About page implementation
Behavior: If user clicks on the "About Me" link on the main page, they will taken to another page.
Parameter: None
'''
@app.route("/about")
def about():
    return render_template("html/about.html")

# By default, the flask web application will run on local machine at the following:
# address: 127.0.0.1 (aka localhost)
# port: 5000
# __main__ basically tells if this file <main.py> is run directly, then run anything that is inside the if block below.
if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 5000, debug = True)