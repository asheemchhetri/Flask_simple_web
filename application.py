from flask import Flask, render_template

# Creating an object for our web-application
# __name__ represents the name of the application package, and it’s used by Flask to identify resources like templates,
# static assets and the instance folder.
# In this case, app package name => application
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
    print(f'The value of __name__ is: {__name__}')
    return render_template("html/home.html")

'''
About page implementation
Behavior: If user clicks on the "About Me" link on the main page, they will taken to another page.
Parameter: None
'''
@app.route("/about")
def about():
    print(f'The value of __name__ is: {__name__}')
    python_info = [
        {
            "name": 'Python',
            "founder": 'Guido van Rossum',
            "status": 'In-Development',
            "version": '3.10.6'
        },
        {
            "name": 'Flask',
            "founder": 'Armin Ronacher',
            "status": 'In-Development',
            "version": '2.2.x'
        },
        {
            "name": 'Django',
            "founder": 'Adrian Holovaty, Simon Willison',
            "status": 'In-Development',
            "version": '4.1'
        },
        {
            "name": 'FastAPI',
            "founder": 'Sebastián Ramírez',
            "status": 'In-Development',
            "version": '0.79.1'
        }
    ]

    return render_template("html/about.html", sample_data=python_info)

'''
Library page implementation
Behavior: If user clicks on the "Library" link on the main page, they will taken to page that shows more amazing python library information.
Parameter: None
'''
@app.route("/library")
def library():
    print(f'The value of __name__ is: {__name__}')
    library_info = [
        {
            "name": '--',
            "founder": '--',
            "status": '--',
            "version": '--'
        }
        # TO-DO: Add more libraries information below
    ]

    return render_template("html/library.html")

# By default, the flask web application will run on local machine at the following:
# address: 127.0.0.1 (aka localhost)
# port: 5000
# __main__ basically tells if this file <main.py> is run directly, then run anything that is inside the if block below.
if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 5000, debug = True)