from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template("Homepage.html")


@app.route('/get_songs', methods=['POST'])
def my_form_post():
    first_name = request.form['firstname']
    songs = str(request.form['subject'])
    print(first_name)
    songs = songs.replace('\r','')
    print(repr(songs))
    names = []
    fw = open("from.txt", "w")
    fw.write(songs)
    fw.close()
    return 'sompleted'


if __name__ == '__main__':
    app.run(debug=True)
