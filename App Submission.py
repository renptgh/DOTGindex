pip install openpyxl 
pip install Flask

from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

template = """
<div class="box {status} {agetag} {parent}{other_placeholder}"
    <img src="{image}" class="image">
    <div class="info">
        <h1>{name}</h1>
        <h2>{byline}</h2>
        <h3>@ {player}</h3>
    </div>
    <div class="hover">
        <div class="text">
            <b>STRENGTH:</b> {STR}</br>
            <b>DEXTERITY:</b> {DEX}</br>
            <b>CONSTITUTION:</b> {CON}</br>
            <b>INTELLIGENCE:</b> {INT}</br>
            <b>WISDOM:</b> {WIS}</br>
            <b>CHARISMA:</b> {CHA}</br></br>
            
            <b>Proficiencies:</b> {profs}</br> 
            <b>Weaknesses:</b> {weak}</br> 
            <b>Abilities:</b> {abilities}</br> 
            <b>Fatal Flaw:</b> {flaw}</br> 
            <b>Magical Items:</b> {items}

            <center>-</center>
            <b>Age:</b> {age}</br> 
            <b>Birthday:</b> {birthday}</br> 
            <b>Pronouns:</b> {pronouns}</br></br>

            <b>Height:</b> {height}</br> 
            <b>Hair Color:</b> {hair}</br> 
            <b>Eye Color:</b> {eyes}</br> 
            <b>Noteworthy Features:</b> {features}</br>
            <b>Faceclaim:</b> {faceclaim}</br>

            <center>-</center>

            <div class="bio"><b>BIOGRAPHY</b></br>{bio}</div></br></br>
        </div> 
    </div> 
</div> 
         <!-------- CHARACTER END -------->
"""            


@app.route('/')
def index():
    return render_template('index.html')


def generate_html(df):
    # Initialize an empty string to store the filled HTML template
    filled_html = ""

    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        other_placeholder = ' ' + row['other'] if row['other'] else ''
            # Fill in the {} placeholders with data from the current row
        filled_html += template.format(
            # Index tags
            status=row['camp status'],
            agetag=row['age tag'],
            parent=row['claimed'],
            other_placeholder=other_placeholder,
            # Index appearance
            image=row['image'],
            name=row['char name'],
            player=row['player'],
            byline=row['byline'],
            # stats
            STR=row['STR'],
            DEX=row['DEX'],
            CON=row['CON'],
            INT=row['INT'],
            WIS=row['WIS'],
            CHA=row['CHA'],
            profs=row['proficiencies'],
            weak=row['weaknesses'],
            abilities=row['abilities'],
            flaw=row['fatal flaw'],
            items=row['items'],
            # about
            age=row['age'],
            birthday=row['birthday'],
            pronouns=row['pronouns'],
            height=row['height'],
            hair=row['hair color'],
            eyes=row['eye color'],
            features=row['features'],
            faceclaim=row['faceclaim'],
            bio=row['bio'],
        )
    # Return the filled HTML template
    return "filled HTML template"


@app.route('/generate', methods=['POST'])
def generate():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']
    if file.filename == '':
        return "No selected file"

    if file:
        df = pd.read_excel(file)
        # Generate filled HTML template
        filled_html = generate_html(df)
        return filled_html


