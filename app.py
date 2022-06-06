from flask import Flask, render_template, request, url_for, flash, redirect
from script import create

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        # gets the link
        link = request.form['link']
        
        # gets the text
        text = request.form['text']
        
        # create the content for the page
        content = create.main(link, text)
        
        # returns the page
        return gitpage(content)
        
    return render_template("index.html")

def gitpage(content):
    return render_template("gitpage.html", content=content)

if __name__ == '__main__':
    app.run(debug=True)
    