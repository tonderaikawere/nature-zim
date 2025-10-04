from flask import Flask, render_template, request, jsonify
import datetime
import random
import os

app = Flask(__name__)
app.secret_key = 'nature_zimbabwe_secret_key_2024'

# Debug route for Vercel
@app.route('/debug')
def debug():
    return {
        'status': 'Flask app is running',
        'python_version': os.sys.version,
        'flask_version': Flask.__version__,
        'routes': [str(rule) for rule in app.url_map.iter_rules()]
    }

# Home and Main Pages
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/partners')
def partners():
    return render_template('partners.html')

@app.route('/support')
def support():
    return render_template('support.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

# Nature & Learning Pages - Grasses
@app.route('/grasses')
def grasses():
    return render_template('nature/grasses.html')

@app.route('/grasses/red-grass')
def red_grass():
    return render_template('nature/grasses/red_grass.html')

@app.route('/grasses/spear-grass')
def spear_grass():
    return render_template('nature/grasses/spear_grass.html')

@app.route('/grasses/elephant-grass')
def elephant_grass():
    return render_template('nature/grasses/elephant_grass.html')

@app.route('/grasses/buffalo-grass')
def buffalo_grass():
    return render_template('nature/grasses/buffalo_grass.html')

@app.route('/grasses/star-grass')
def star_grass():
    return render_template('nature/grasses/star_grass.html')

# Nature & Learning Pages - Trees
@app.route('/trees')
def trees():
    return render_template('nature/trees.html')

@app.route('/trees/baobab')
def baobab():
    return render_template('nature/trees/baobab.html')

@app.route('/trees/msasa')
def msasa():
    return render_template('nature/trees/msasa.html')

@app.route('/trees/mopane')
def mopane():
    return render_template('nature/trees/mopane.html')

@app.route('/trees/acacia')
def acacia():
    return render_template('nature/trees/acacia.html')

@app.route('/trees/mahogany')
def mahogany():
    return render_template('nature/trees/mahogany.html')

# Nature & Learning Pages - Flowers
@app.route('/flowers')
def flowers():
    return render_template('nature/flowers.html')

@app.route('/flowers/flame-lily')
def flame_lily():
    return render_template('nature/flowers/flame_lily.html')

@app.route('/flowers/orchid')
def orchid():
    return render_template('nature/flowers/orchid.html')

@app.route('/flowers/sunflower')
def sunflower():
    return render_template('nature/flowers/sunflower.html')

# Nature & Learning Pages - Birds
@app.route('/birds')
def birds():
    return render_template('nature/birds.html')

@app.route('/birds/african-fish-eagle')
def african_fish_eagle():
    return render_template('nature/birds/african_fish_eagle.html')

@app.route('/birds/hornbill')
def hornbill():
    return render_template('nature/birds/hornbill.html')

@app.route('/birds/weaver-bird')
def weaver_bird():
    return render_template('nature/birds/weaver_bird.html')

# Nature & Learning Pages - Mammals
@app.route('/mammals')
def mammals():
    return render_template('nature/mammals.html')

@app.route('/mammals/elephant')
def elephant():
    return render_template('nature/mammals/elephant.html')

@app.route('/mammals/lion')
def lion():
    return render_template('nature/mammals/lion.html')

@app.route('/mammals/zebra')
def zebra():
    return render_template('nature/mammals/zebra.html')

# Nature & Learning Pages - Reptiles
@app.route('/reptiles')
def reptiles():
    return render_template('nature/reptiles.html')

@app.route('/reptiles/crocodile')
def crocodile():
    return render_template('nature/reptiles/crocodile.html')

@app.route('/reptiles/python')
def python():
    return render_template('nature/reptiles/python.html')

@app.route('/reptiles/chameleon')
def chameleon():
    return render_template('nature/reptiles/chameleon.html')

# Nature & Learning Pages - Insects
@app.route('/insects')
def insects():
    return render_template('nature/insects.html')

@app.route('/insects/butterfly')
def butterfly():
    return render_template('nature/insects/butterfly.html')

@app.route('/insects/bee')
def bee():
    return render_template('nature/insects/bee.html')

@app.route('/insects/ant')
def ant():
    return render_template('nature/insects/ant.html')

# Nature & Learning Pages - Fish
@app.route('/fish')
def fish():
    return render_template('nature/fish.html')

@app.route('/fish/tilapia')
def tilapia():
    return render_template('nature/fish/tilapia.html')

@app.route('/fish/catfish')
def catfish():
    return render_template('nature/fish/catfish.html')

# Nature & Learning Pages - Rivers & Lakes
@app.route('/rivers-lakes')
def rivers_lakes():
    return render_template('nature/rivers_lakes.html')

@app.route('/rivers-lakes/zambezi')
def zambezi():
    return render_template('nature/rivers_lakes/zambezi.html')

@app.route('/rivers-lakes/lake-kariba')
def lake_kariba():
    return render_template('nature/rivers_lakes/lake_kariba.html')

# Nature & Learning Pages - National Parks
@app.route('/national-parks')
def national_parks():
    return render_template('nature/national_parks.html')

@app.route('/national-parks/hwange')
def hwange():
    return render_template('nature/national_parks/hwange.html')

@app.route('/national-parks/mana-pools')
def mana_pools():
    return render_template('nature/national_parks/mana_pools.html')

@app.route('/national-parks/matobo')
def matobo():
    return render_template('nature/national_parks/matobo.html')

# Additional Nature Pages
@app.route('/climate-seasons')
def climate_seasons():
    return render_template('nature/climate_seasons.html')

@app.route('/soils-agriculture')
def soils_agriculture():
    return render_template('nature/soils_agriculture.html')

@app.route('/habitats-ecosystems')
def habitats_ecosystems():
    return render_template('nature/habitats_ecosystems.html')

@app.route('/conservation')
def conservation():
    return render_template('nature/conservation.html')

@app.route('/culture-nature')
def culture_nature():
    return render_template('nature/culture_nature.html')

# Games Section
@app.route('/games')
def games_home():
    return render_template('games/games_home.html')

@app.route('/games/dice-roller')
def dice_roller():
    return render_template('games/dice_roller.html')

@app.route('/games/quiz')
def quiz_game():
    return render_template('games/quiz_game.html')

@app.route('/games/puzzle')
def puzzle():
    return render_template('games/puzzle.html')

@app.route('/games/word-search')
def word_search():
    return render_template('games/word_search.html')

@app.route('/games/memory-match')
def memory_match():
    return render_template('games/memory_match.html')

@app.route('/games/nature-trivia')
def nature_trivia():
    return render_template('games/nature_trivia.html')

@app.route('/games/animal-sounds')
def animal_sounds():
    return render_template('games/animal_sounds.html')

@app.route('/games/grass-id-challenge')
def grass_id_challenge():
    return render_template('games/grass_id_challenge.html')

@app.route('/games/wildlife-flashcards')
def wildlife_flashcards():
    return render_template('games/wildlife_flashcards.html')

@app.route('/games/scoreboard')
def scoreboard():
    return render_template('games/scoreboard.html')

# Tools Section
@app.route('/tools')
def tools_home():
    return render_template('tools/tools_home.html')

@app.route('/tools/calculator')
def calculator():
    return render_template('tools/calculator.html')

@app.route('/tools/age-calculator')
def age_calculator():
    return render_template('tools/age_calculator.html')

@app.route('/tools/calendar')
def calendar_viewer():
    return render_template('tools/calendar.html')

@app.route('/tools/temperature-converter')
def temperature_converter():
    return render_template('tools/temperature_converter.html')

@app.route('/tools/length-converter')
def length_converter():
    return render_template('tools/length_converter.html')

@app.route('/tools/weight-converter')
def weight_converter():
    return render_template('tools/weight_converter.html')

@app.route('/tools/bmi-calculator')
def bmi_calculator():
    return render_template('tools/bmi_calculator.html')

@app.route('/tools/currency-converter')
def currency_converter():
    return render_template('tools/currency_converter.html')

@app.route('/tools/todo-list')
def todo_list():
    return render_template('tools/todo_list.html')

@app.route('/tools/notes')
def notes_app():
    return render_template('tools/notes.html')

@app.route('/tools/stopwatch')
def stopwatch():
    return render_template('tools/stopwatch.html')

# API endpoints for games and tools
@app.route('/api/roll-dice')
def roll_dice():
    sides = request.args.get('sides', 6, type=int)
    result = random.randint(1, sides)
    return jsonify({'result': result})

@app.route('/api/calculate-age', methods=['POST'])
def calculate_age():
    data = request.get_json()
    birth_date = datetime.datetime.strptime(data['birth_date'], '%Y-%m-%d')
    today = datetime.datetime.now()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return jsonify({'age': age})

@app.route('/api/convert-temperature', methods=['POST'])
def convert_temperature():
    data = request.get_json()
    temp = float(data['temperature'])
    from_unit = data['from_unit']
    to_unit = data['to_unit']
    
    # Convert to Celsius first
    if from_unit == 'fahrenheit':
        celsius = (temp - 32) * 5/9
    elif from_unit == 'kelvin':
        celsius = temp - 273.15
    else:
        celsius = temp
    
    # Convert from Celsius to target unit
    if to_unit == 'fahrenheit':
        result = celsius * 9/5 + 32
    elif to_unit == 'kelvin':
        result = celsius + 273.15
    else:
        result = celsius
    
    return jsonify({'result': round(result, 2)})

# SEO and Technical Routes
@app.route('/robots.txt')
def robots_txt():
    return app.send_static_file('robots.txt')

@app.route('/sitemap.xml')
def sitemap_xml():
    return app.send_static_file('sitemap.xml')

@app.route('/site.webmanifest')
def webmanifest():
    return app.send_static_file('site.webmanifest')

@app.route('/favicon.ico')
def favicon_ico():
    return app.send_static_file('favicon.ico')

@app.route('/favicon.svg')
def favicon_svg():
    return app.send_static_file('favicon.svg')

# For Vercel deployment
if __name__ == '__main__':
    app.run(debug=True)

# Export the app for Vercel
application = app
