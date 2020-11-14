import os
from flask import Flask, redirect, url_for, request, send_file, render_template
from gifgen import generator
app = Flask(__name__)

colors = generator.all_colors
skins = generator.all_skins

@app.route("/", methods=['GET', 'POST'])
def hello():
    return redirect('/ejection')

@app.route("/ejection", methods=['GET', 'POST'])
def ejection():
    if request.method == 'POST':
        data = request.form
        impostor = True if data['impostor'] == 'True' else (False if data['impostor'] == 'False' else (None if data['impostor'] == 'None' else 'rand'))
        color = data['color'] if data['color'] != 'None' else None
        skin = data['skin'] if data['skin'] != 'None' else None
        person = data['person']
        gif_name = generator.generate_ejection_message(color=color, skn=skin, impostor=impostor, path='./gifs', person=person)
        return redirect('gif/'+gif_name)
    else:
        return render_template('ejection.html')

@app.route("/message", methods=['GET', 'POST'])
def message():
    if request.method == 'POST':
        data = request.form
        color = data['color'] if data['color'] != 'None' else None
        skin = data['skin'] if data['skin'] != 'None' else None
        text = data['text']
        gif_name = generator.generate_ejection_custom_message(color=color, skn=skin, text=text, path='./gifs')
        return redirect('gif/'+gif_name)
    else:
        return render_template('message.html')

@app.route("/gif/<gif>")
def display_fig(gif):
    return send_file('gifs/' + gif, mimetype='image/gif')


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)