from flask import Flask, render_template
app = Flask(__name__)

@app.route('/checkerboard')
def checkerboard():
    return render_template('index.html')

@app.route('/checkerboard/<int:x>/<int:y>')
def checkerboard_rows(x, y):
    return render_template('index.html', x=x, y=y)

if __name__=="__main__":
    app.run(debug=True)