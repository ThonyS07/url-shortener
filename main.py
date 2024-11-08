from flask import Flask, render_template, request
import pyshorteners
app= Flask(__name__)
@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        received_url = request.form['url']
        short_url = pyshorteners.Shortener().tinyurl.short(received_url)
        return render_template('form.html', new_url = short_url, old_url = received_url)
    else:
        return render_template('form.html')

if __name__ == '__main__':
    app.run()