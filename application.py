from flask import Flask, request

app = Flask(__name__)

@app.route("/application")
def index_page():
    # Return this as a strange
    firstname = request.args.get("firstname")
    lastname = request.args.get("lastname")
    job = request.args.get("job")
    salary = request.args.get("salary")

    return """
    <html>
    <body>
    	Thank you, {{ firstname }} {{ lastname}}, for applying to be a {{ job  }}.
    	Your minimum salary requirement is {{ salary }} dollars.
	</body>
	</html>
	"""

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)