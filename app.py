from flask import Flask, render_template, request, url_for, flash, redirect
from script import create

app = Flask(__name__)

messages = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Two Content'}
            ]


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        link = request.form['link']
        text = request.form['text']
        content = create.main(link, text)
        return gitpage(content)
        
    return render_template("index.html", messages=messages)

def gitpage(content):
    return render_template("gitpage.html", content=content)

if __name__ == '__main__':
    app.run(debug=True)
    