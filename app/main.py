import os

import gifgen.generator
from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import send_file

app = Flask(__name__)

colors = gifgen.generator.all_colors
light_colors = (
    'red', 'blue', 'pink', 'orange', 'black',
    'purple', 'brown', 'maroon', 'gray',
)


@app.route('/', methods=['GET', 'POST'])
def hello():  # dead: disable
    return redirect('/ejection')


@app.route('/ejection', methods=['GET', 'POST'])
def ejection():  # dead: disable
    if request.method == 'POST':
        data = request.form
        impostor = True if data['impostor'] == 'True' else (
            False if data['impostor'] == 'False' else (
                None if data['impostor'] == 'None' else 'rand'
            )
        )
        color = data['color'] if data['color'] != 'None' else None
        skin = data['skin'] if data['skin'] != 'None' else None
        person = data['person']
        gif_name = gifgen.generator.generate_ejection_message(
            color=color, skn=skin, impostor=impostor, path='./gifs', person=person,
        )
        return redirect('gif/'+gif_name)
    else:
        return render_template('ejection.html', colors=colors, light_colors=light_colors)


@app.route('/message', methods=['GET', 'POST'])
def message():  # dead: disable
    if request.method == 'POST':
        data = request.form
        color = data['color'] if data['color'] != 'None' else None
        skin = data['skin'] if data['skin'] != 'None' else None
        text = data['text']
        gif_name = gifgen.generator.generate_ejection_custom_message(
            color=color, skn=skin, text=text, path='./gifs',
        )
        return redirect('gif/'+gif_name)
    else:
        return render_template('message.html', colors=colors, light_colors=light_colors)


@app.route('/gif/<gif>')
def display_fig(gif):  # dead: disable
    return send_file('gifs/' + gif, mimetype='image/gif')


if __name__ == '__main__':
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
