# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template, request, url_for
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello Lutsk!"


@app.route("/lutskio")
def lutskio():
    topics = [
              u"Розробка ігор під iOS на Unreal Developer's Kit",
              u"Розробка ігор під iOS/Android/Kindle/Nook на Corona SDK",
              u"Використання node.js у веб девелопменті",
              u"Erlang/Mochiweb із з чим його їдять"
              ]

    context = {
        'page_title': u"Теми lutsk.io",
        'topics': topics,
    }
    return render_template('lutskio.html', **context)


if __name__ == "__main__":
    app.run(debug=True)