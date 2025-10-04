from flask import Flask, render_template, request, jsonify
import datetime
import random
import os

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.secret_key = 'nature_zimbabwe_secret_key_2024'

# Home and Main Pages
@app.route('/')
def home():
    try:
        return render_template('home.html')
    except Exception as e:
        return f'''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Nature Zimbabwe - Tonde's Educational Platform</title>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
            <style>
                :root {{
                    --nature-green: #2D5016;
                    --nature-light-green: #4A7C59;
                    --nature-gold: #D4AF37;
                }}
                body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }}
                .hero-section {{
                    background: linear-gradient(135deg, var(--nature-green) 0%, var(--nature-light-green) 100%);
                    color: white;
                    min-height: 100vh;
                    display: flex;
                    align-items: center;
                }}
                .btn-nature {{
                    background: linear-gradient(135deg, var(--nature-green), var(--nature-light-green));
                    border: none;
                    color: white !important;
                    font-weight: 500;
                    padding: 0.75rem 2rem;
                    border-radius: 25px;
                    transition: all 0.3s ease;
                    text-decoration: none;
                    display: inline-block;
                }}
                .btn-nature:hover {{
                    transform: translateY(-2px);
                    box-shadow: 0 4px 12px rgba(45, 80, 22, 0.3);
                }}
            </style>
        </head>
        <body>
            <section class="hero-section">
                <div class="container">
                    <div class="row align-items-center">
                        <div class="col-lg-6">
                            <h1 class="display-4 fw-bold mb-4">🌳 Welcome to Nature Zimbabwe</h1>
                            <p class="lead mb-4">Discover the incredible biodiversity and natural wonders of Zimbabwe. From the iconic Baobab trees to the diverse wildlife that roams our beautiful landscapes.</p>
                            <p class="mb-4"><strong>Created by Tonde Kawere</strong> with a dream to educate people about Zimbabwe's incredible natural heritage.</p>
                            <div class="d-flex flex-wrap gap-3">
                                <a href="/trees" class="btn btn-nature">🌳 Explore Nature</a>
                                <a href="/games" class="btn btn-nature">🎮 Play Games</a>
                            </div>
                        </div>
                        <div class="col-lg-6 text-center">
                            <div style="font-size: 8rem;">🌳</div>
                        </div>
                    </div>
                </div>
            </section>
            
            <div class="container py-5">
                <div class="row">
                    <div class="col-md-4 mb-4">
                        <div class="card h-100 border-0 shadow-sm">
                            <div class="card-body text-center">
                                <div class="mb-3" style="font-size: 3rem;">🎮</div>
                                <h5 class="card-title">Educational Games</h5>
                                <p class="card-text">Learn through fun and interactive games about Zimbabwe's wildlife.</p>
                                <a href="/games" class="btn btn-nature">Play Now</a>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-4 mb-4">
                        <div class="card h-100 border-0 shadow-sm">
                            <div class="card-body text-center">
                                <div class="mb-3" style="font-size: 3rem;">🌿</div>
                                <h5 class="card-title">Explore Nature</h5>
                                <p class="card-text">Discover Zimbabwe's rich biodiversity and natural heritage.</p>
                                <a href="/trees" class="btn btn-nature">Explore</a>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-4 mb-4">
                        <div class="card h-100 border-0 shadow-sm">
                            <div class="card-body text-center">
                                <div class="mb-3" style="font-size: 3rem;">🏞️</div>
                                <h5 class="card-title">National Parks</h5>
                                <p class="card-text">Explore Zimbabwe's protected areas and conservation efforts.</p>
                                <a href="/national-parks" class="btn btn-nature">Visit Parks</a>
                            </div>
                        </div>
                    </div>
                </div>
                
                <hr class="my-5">
                <div class="text-center">
                    <p class="lead"><em>Created with ❤️ by <strong>Tonde Kawere</strong> to share Zimbabwe's natural wonders with the world.</em></p>
                    <p><strong>Mission:</strong> To educate people about nature and promote conservation awareness.</p>
                </div>
            </div>
            
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
        </body>
        </html>
        '''

@app.route('/about')
def about():
    try:
        return render_template('about.html')
    except:
        return '''
        <h1>About Nature Zimbabwe</h1>
        <p>Created by Tonde Kawere to educate people about Zimbabwe's natural heritage.</p>
        <a href="/">Back to Home</a>
        '''

@app.route('/contact')
def contact():
    try:
        return render_template('contact.html')
    except:
        return '''
        <h1>Contact Us</h1>
        <p>Get in touch with Tonde about Nature Zimbabwe.</p>
        <a href="/">Back to Home</a>
        '''

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
    try:
        return render_template('games/games_home.html')
    except:
        return '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Educational Games - Nature Zimbabwe</title>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
            <style>
                :root { --nature-green: #2D5016; --nature-light-green: #4A7C59; }
                .btn-nature { background: linear-gradient(135deg, var(--nature-green), var(--nature-light-green)); border: none; color: white !important; padding: 0.75rem 2rem; border-radius: 25px; text-decoration: none; }
                .game-card { border: 2px solid var(--nature-green); padding: 20px; margin: 15px 0; border-radius: 10px; }
            </style>
        </head>
        <body>
            <div class="container py-5">
                <h1 class="text-center mb-5" style="color: var(--nature-green);">🎮 Educational Wildlife Games</h1>
                <p class="text-center lead">Learn about Zimbabwe's wildlife through fun and interactive games created by Tonde!</p>
                
                <div class="row">
                    <div class="col-md-6 mb-4">
                        <div class="game-card">
                            <h3>🔊 Animal Sounds Quiz</h3>
                            <p>Test your knowledge of Zimbabwe's wildlife! Listen to animal sounds and identify which animal makes each sound.</p>
                            <a href="/games/animal-sounds" class="btn btn-nature">Play Now</a>
                        </div>
                    </div>
                    <div class="col-md-6 mb-4">
                        <div class="game-card">
                            <h3>🧠 Nature Trivia</h3>
                            <p>Challenge yourself with questions about Zimbabwe's flora, fauna, and national parks.</p>
                            <a href="/games/quiz" class="btn btn-nature">Coming Soon</a>
                        </div>
                    </div>
                </div>
                
                <div class="text-center mt-4">
                    <a href="/" class="btn btn-nature">🏠 Back to Home</a>
                </div>
            </div>
        </body>
        </html>
        '''

@app.route('/games/animal-sounds')
def animal_sounds():
    try:
        return render_template('games/animal_sounds.html')
    except:
        return '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Zimbabwe Animal Sounds Quiz - Nature Zimbabwe</title>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
            <style>
                :root { --nature-green: #2D5016; --nature-light-green: #4A7C59; }
                .btn-nature { background: linear-gradient(135deg, var(--nature-green), var(--nature-light-green)); border: none; color: white !important; padding: 15px 30px; border-radius: 5px; margin: 10px; cursor: pointer; font-size: 16px; text-decoration: none; }
                .animal-btn { background: var(--nature-light-green); color: white; padding: 15px; border-radius: 8px; border: none; margin: 5px; cursor: pointer; }
                #sound-description { background: #e8f5e8; padding: 15px; border-radius: 5px; margin: 20px 0; }
            </style>
        </head>
        <body>
            <div class="container py-5">
                <h1 class="text-center mb-4" style="color: var(--nature-green);">🔊 Zimbabwe Animal Sounds Quiz</h1>
                <p class="text-center">Created by Tonde to help you learn about Zimbabwe's amazing wildlife!</p>
                
                <div class="text-center">
                    <div id="sound-description">
                        <p>🎯 <strong>How to Play:</strong></p>
                        <p>1. Click "Play Sound" to hear an animal sound</p>
                        <p>2. Choose which animal you think makes that sound</p>
                        <p>3. Learn about Zimbabwe's incredible wildlife!</p>
                    </div>
                    
                    <button class="btn btn-nature" onclick="playRandomSound()">🔊 Play Sound</button>
                    <button class="btn btn-nature" onclick="testAudio()">🎵 Test Audio</button>
                    
                    <div class="row mt-4">
                        <div class="col-md-4 mb-2"><button class="animal-btn w-100" onclick="selectAnimal('Lion')">🦁 Lion</button></div>
                        <div class="col-md-4 mb-2"><button class="animal-btn w-100" onclick="selectAnimal('Elephant')">🐘 Elephant</button></div>
                        <div class="col-md-4 mb-2"><button class="animal-btn w-100" onclick="selectAnimal('Hippo')">🦛 Hippo</button></div>
                        <div class="col-md-4 mb-2"><button class="animal-btn w-100" onclick="selectAnimal('Zebra')">🦓 Zebra</button></div>
                        <div class="col-md-4 mb-2"><button class="animal-btn w-100" onclick="selectAnimal('Hyena')">🐺 Hyena</button></div>
                        <div class="col-md-4 mb-2"><button class="animal-btn w-100" onclick="selectAnimal('African Fish Eagle')">🦅 Fish Eagle</button></div>
                    </div>
                    
                    <div id="result" style="margin: 20px 0; font-size: 18px;"></div>
                    
                    <a href="/games" class="btn btn-nature">🎮 Back to Games</a>
                    <a href="/" class="btn btn-nature">🏠 Home</a>
                </div>
            </div>
            
            <script>
                const animals = [
                    {name: 'Lion', sound: 'Deep, powerful roar that can be heard from miles away', emoji: '🦁'},
                    {name: 'Elephant', sound: 'Trumpeting call and low rumbling sounds', emoji: '🐘'},
                    {name: 'Hippo', sound: 'Deep grunting and snorting sounds', emoji: '🦛'},
                    {name: 'Zebra', sound: 'Barking and whinnying like a horse', emoji: '🦓'},
                    {name: 'Hyena', sound: 'Distinctive laughing and whooping calls', emoji: '🐺'},
                    {name: 'African Fish Eagle', sound: 'High-pitched, distinctive call over water', emoji: '🦅'}
                ];
                
                let currentAnimal = null;
                
                function playRandomSound() {
                    currentAnimal = animals[Math.floor(Math.random() * animals.length)];
                    document.getElementById('sound-description').innerHTML = 
                        '<p>🔊 <strong>Listen:</strong> ' + currentAnimal.sound + '</p>' +
                        '<p>Which animal makes this sound?</p>';
                    playSyntheticSound(currentAnimal.name);
                }
                
                function playSyntheticSound(animalName) {
                    try {
                        const audioContext = new (window.AudioContext || window.webkitAudioContext)();
                        if (audioContext.state === 'suspended') audioContext.resume();
                        
                        const oscillator = audioContext.createOscillator();
                        const gainNode = audioContext.createGain();
                        oscillator.connect(gainNode);
                        gainNode.connect(audioContext.destination);
                        
                        let frequency = 440, duration = 1;
                        switch(animalName.toLowerCase()) {
                            case 'lion': frequency = 120; duration = 2; break;
                            case 'elephant': frequency = 300; duration = 1.5; break;
                            case 'hippo': frequency = 150; duration = 1.2; break;
                            case 'zebra': frequency = 250; duration = 0.8; break;
                            case 'hyena': frequency = 400; duration = 1.5; break;
                            case 'african fish eagle': frequency = 800; duration = 1; break;
                        }
                        
                        oscillator.frequency.setValueAtTime(frequency, audioContext.currentTime);
                        gainNode.gain.setValueAtTime(0, audioContext.currentTime);
                        gainNode.gain.linearRampToValueAtTime(0.3, audioContext.currentTime + 0.1);
                        gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + duration);
                        
                        oscillator.start(audioContext.currentTime);
                        oscillator.stop(audioContext.currentTime + duration);
                    } catch (error) {
                        console.log('Audio not supported:', error);
                    }
                }
                
                function testAudio() {
                    try {
                        const audioContext = new (window.AudioContext || window.webkitAudioContext)();
                        const oscillator = audioContext.createOscillator();
                        const gainNode = audioContext.createGain();
                        
                        oscillator.connect(gainNode);
                        gainNode.connect(audioContext.destination);
                        oscillator.frequency.setValueAtTime(440, audioContext.currentTime);
                        gainNode.gain.setValueAtTime(0, audioContext.currentTime);
                        gainNode.gain.linearRampToValueAtTime(0.3, audioContext.currentTime + 0.01);
                        gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.5);
                        
                        oscillator.start(audioContext.currentTime);
                        oscillator.stop(audioContext.currentTime + 0.5);
                        alert('If you heard a beep, audio is working!');
                    } catch (error) {
                        alert('Audio not supported: ' + error.message);
                    }
                }
                
                function selectAnimal(selectedAnimal) {
                    if (!currentAnimal) {
                        document.getElementById('result').innerHTML = '<p style="color: orange;">🔊 Please play a sound first!</p>';
                        return;
                    }
                    
                    const isCorrect = selectedAnimal === currentAnimal.name;
                    const resultDiv = document.getElementById('result');
                    
                    if (isCorrect) {
                        resultDiv.innerHTML = '<p style="color: green;">🎉 Correct! That was a ' + currentAnimal.name + ' ' + currentAnimal.emoji + '</p><p>' + currentAnimal.sound + '</p>';
                    } else {
                        resultDiv.innerHTML = '<p style="color: red;">❌ Not quite! That was a ' + currentAnimal.name + ' ' + currentAnimal.emoji + '</p><p>' + currentAnimal.sound + '</p>';
                    }
                    
                    setTimeout(() => {
                        currentAnimal = null;
                        document.getElementById('sound-description').innerHTML = '<p>🎯 Ready for the next challenge? Click "Play Sound" to continue!</p>';
                    }, 3000);
                }
            </script>
        </body>
        </html>
        '''

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

# Export for Vercel
application = app
