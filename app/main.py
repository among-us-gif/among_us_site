from flask import Flask, redirect, url_for, request, send_file
from gifgen import generator
app = Flask(__name__)

colors = generator.all_colors
skins = generator.all_skins

@app.route("/", methods=['GET'])
def hello():
    return '''
    <html>
        <head>
            <title>Among Us GIF Generator</title>
        </head>
        <body>
            <form action="/" method="POST">
                <label for="person">Name</label>
                <input type="text" name="person"><br><br>
                <label for="color">Color</label>
                <select name="color">
                    <option selected value="None">Random</option>
                    <option value="red">Red</option>
                    <option value="blue">Blue</option>
                    <option value="green">Green</option>
                    <option value="pink">Pink</option>
                    <option value="orange">Orange</option>
                    <option value="yellow">Yellow</option>
                    <option value="grey">Black</option>
                    <option value="white">White</option>
                    <option value="purple">Purple</option>
                    <option value="brown">Brown</option>
                    <option value="cyan">Cyan</option>
                    <option value="lime">Lime</option>
                </select><br><br>
                <label for="skin">Skin</label>
                <select name="skin">
                    <option selected value="None">No Skin</option>
                    <option value="rand">Random</option>
                    <option value="archae">Archaeologist</option>
                    <option value="astro">Astronaut</option>
                    <option value="capt">Captain</option>
                    <option value="hazmat">Hazmat Suit</option>
                    <option value="mech">Mechanic</option>
                    <option value="military">Military Uniform</option>
                    <option value="miner">Miner</option>
                    <option value="police>Police Officer</option>
                    <option value="secguard">Security Guard</option>
                    <option value="science">Doctor</option>
                    <option value="blacksuit">Black Suit</option>
                    <option value="whitesuit">White Suit</option>
                    <option value="tarmac">Tarmac Worker</option>
                    <option value="wall">Wall Guard Suit</option>
                    <option value="winter">Winter Attire</option>
                </select><br><br>
                <label for="impostor">Impostor</label>
                <select name="impostor">
                    <option value="True">Yes</option>
                    <option value="False">No</option>
                    <option value="None">Unknown</option>
                </select><br><br>
                <input type="submit" value="Submit">
            </form>
        </body>
    </html>
    '''

@app.route("/", methods=['POST'])
def process():
    if request.method == 'POST':
        data = request.form
        impostor = True if data['impostor'] == 'True' else (False if data['impostor'] == 'False' else None)
        color = data['color'] if data['color'] != 'None' else None
        skin = data['skin'] if data['skin'] != 'None' else None
        person = data['person']
        gif_name = generator.generate_ejection_message(color=color, skn=skin, impostor=impostor, path='./gifs', person=person)
        print(gif_name)
        return redirect('gif/'+gif_name)
        #return redirect('/')

@app.route("/gif/<gif>")
def display_fig(gif):
    return send_file('gifs/' + gif, mimetype='image/gif')


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)