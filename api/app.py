from flask import Flask, render_template, request, jsonify
import datetime
import random
import os

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.secret_key = 'nature_zimbabwe_secret_key_2024'

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

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

# Nature Categories
@app.route('/grasses')
def grasses():
    return render_template('nature/grasses.html')

@app.route('/trees')
def trees():
    return render_template('nature/trees.html')

@app.route('/flowers')
def flowers():
    return render_template('nature/flowers.html')

@app.route('/birds')
def birds():
    return render_template('nature/birds.html')

@app.route('/mammals')
def mammals():
    return render_template('nature/mammals.html')

@app.route('/reptiles')
def reptiles():
    return render_template('nature/reptiles.html')

@app.route('/insects')
def insects():
    return render_template('nature/insects.html')

@app.route('/fish')
def fish():
    return render_template('nature/fish.html')

@app.route('/national-parks')
def national_parks():
    return render_template('nature/national_parks.html')

# Specific Nature Pages
@app.route('/trees/baobab')
def baobab():
    return render_template('nature/trees/baobab.html')

@app.route('/trees/msasa')
def msasa():
    return render_template('nature/trees/msasa.html')

@app.route('/mammals/elephant')
def elephant():
    return render_template('nature/mammals/elephant.html')

@app.route('/mammals/lion')
def lion():
    return render_template('nature/mammals/lion.html')

@app.route('/mammals/zebra')
def zebra():
    return render_template('nature/mammals/zebra.html')

@app.route('/birds/african-fish-eagle')
def african_fish_eagle():
    return render_template('nature/birds/african_fish_eagle.html')

@app.route('/national-parks/hwange')
def hwange():
    return render_template('nature/national_parks/hwange.html')

@app.route('/national-parks/mana-pools')
def mana_pools():
    return render_template('nature/national_parks/mana_pools.html')

@app.route('/national-parks/matobo')
def matobo():
    return render_template('nature/national_parks/matobo.html')

# Games Section
@app.route('/games')
def games_home():
    return render_template('games/games_home.html')

@app.route('/games/animal-sounds')
def animal_sounds():
    return render_template('games/animal_sounds.html')

@app.route('/games/quiz')
def quiz():
    return render_template('games/quiz.html')

@app.route('/games/nature-trivia')
def nature_trivia():
    return render_template('games/nature_trivia.html')

@app.route('/games/memory-match')
def memory_match():
    return render_template('games/memory_match.html')

# Tools Section
@app.route('/tools')
def tools():
    return render_template('tools/tools_home.html')

@app.route('/tools/calculator')
def calculator():
    return render_template('tools/calculator.html')

@app.route('/tools/currency-converter')
def currency_converter():
    return render_template('tools/currency_converter.html')

# Additional Pages
@app.route('/conservation')
def conservation():
    return render_template('conservation.html')

@app.route('/climate-seasons')
def climate_seasons():
    return render_template('climate_seasons.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

# API Routes for Tools
@app.route('/api/convert-currency', methods=['POST'])
def convert_currency():
    data = request.get_json()
    amount = float(data['amount'])
    from_currency = data['from_currency']
    to_currency = data['to_currency']
    
    # Simple exchange rates (in production, use real API)
    rates = {
        'USD': 1.0,
        'ZWL': 25.0,  # Zimbabwe Dollar (historical)
        'ZAR': 18.5,  # South African Rand
        'BWP': 13.5,  # Botswana Pula
        'EUR': 0.85,
        'GBP': 0.73
    }
    
    # Convert to USD first, then to target currency
    usd_amount = amount / rates.get(from_currency, 1)
    result = usd_amount * rates.get(to_currency, 1)
    
    return jsonify({'result': round(result, 2)})

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

# Debug route
@app.route('/debug')
def debug():
    return {
        'status': 'Flask app is running on Vercel',
        'creator': 'Tonde Kawere',
        'mission': 'To educate people about Zimbabwe nature',
        'template_folder': app.template_folder,
        'static_folder': app.static_folder,
        'routes': [str(rule) for rule in app.url_map.iter_rules()]
    }

# This is crucial for Vercel
if __name__ == '__main__':
    app.run(debug=True)
