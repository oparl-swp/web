from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    """Render welcome template containing post form and information."""
    return render_template('welcome.htm')

@app.route('/about')
def about():
    """About page containing some information."""
    return render_template('about.htm')

@app.route('/validate', methods=['POST'])
def validate_post():
    """Validate posted JSON"""
    return render_template('validate.htm', original=request.form['input'])

@app.route('/validate/<path:url>')
def validate_from_url():
    return 'not implemented yet'

def run():
    app.run(debug=True) # TODO: remove debugging
