from flask import Flask
from flask import Flask,abort, flash, redirect, render_template, request, session
from tempfile import mkdtemp
from algorithms import *
  
# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response 




  
# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route("/", methods=[ "POST"])
def index():
    data=rating()
    data2=genre('romance')
    data3=genre('thriller')
    if request.method=="POST":
        search= request.form.get("input")
        data1= final_recom(search)
        return render_template("index.html", data=data, data1=data1, data2=data2, data3=data3)
        


    
    return render_template("index.html", data=data, data2=data2, data3=data3)


# main driver function
if __name__ == '__main__':
  
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(debug=True)    