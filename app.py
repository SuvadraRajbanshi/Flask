from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/start")
def start():
    return render_template('start.html')  


@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/farmer")
def farmer():
    return render_template('farmer.html')

@app.route("/admin")
def admin():
    return render_template('admin.html')

@app.route("/expert")
def expert():
    return render_template('expert.html')

@app.route("/fregister")
def fregister():
    return render_template('f-reg.html')

@app.route("/fpage")
def fpage():
    return render_template('f-page.html')

@app.route("/fproblem")
def fproblem():
    return render_template('f-problem.html')

@app.route("/fimage")
def fimage():
    return render_template('f-image.html')

@app.route("/fsolution")
def fsolution():
    return render_template('f-solution.html')

    

if __name__ == "__main__":
    app.run(debug=True) 