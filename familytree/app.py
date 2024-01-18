# importing modules from flask library
from flask import Flask, render_template

# creating an instance of the Flask class, by providing __name__ keyword as an argument
app = Flask(__name__)

# write the routes using decorator functions

# default route or 'URL'
@app.route("/")
def home():
    name = "Your Name"  # write your name
    age = "Your Age"    # write your age
    return render_template('index.html', name=name, age=age)

# define the route to father webpage
@app.route("/father")
def father():
    father_name = "Father's Name"
    father_age = "Father's Age"
    return render_template('father.html', name=father_name, age=father_age)

# define the route to mother webpage
@app.route("/mother")
def mother():
    mother_name = "Mother's Name"
    mother_age = "Mother's Age"
    return render_template('mother.html', name=mother_name, age=mother_age)

# define the route to friends webpage
@app.route("/friends")
def friends():
    # You can customize this section based on the information you want to display for friends
    friend_name = "Friend's Name"
    friend_age = "Friend's Age"
    return render_template('friends.html', name=friend_name, age=friend_age)

# add other routes, if you want

# run the file
if __name__ == '__main__':
    app.run(debug=True)
