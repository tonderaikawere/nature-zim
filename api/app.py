from flask import Flask, render_template, request, jsonify
import datetime
import random
import os

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.secret_key = 'nature_zimbabwe_secret_key_2024'

# Test route
@app.route('/')
def home():
    try:
        return render_template('home.html')
    except Exception as e:
        return f'''
        <h1>Nature Zimbabwe - Tonde's Educational Platform</h1>
        <p>Welcome to Nature Zimbabwe! Created by Tonde to educate people about Zimbabwe's incredible wildlife and nature.</p>
        <p>Template error: {str(e)}</p>
        <p><a href="/simple">Try Simple Version</a></p>
        '''

@app.route('/simple')
def simple():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Nature Zimbabwe - Tonde's Educational Platform</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }
            .container { max-width: 800px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; }
            h1 { color: #2D5016; }
            .btn { background: #2D5016; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; display: inline-block; margin: 10px 5px; }
            .btn:hover { background: #4A7C59; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🌳 Nature Zimbabwe</h1>
            <h2>Tonde's Educational Journey Through Zimbabwe's Wildlife</h2>
            <p>Welcome to Nature Zimbabwe! This platform was created by <strong>Tonde Kawere</strong> with a dream to educate people about Zimbabwe's incredible natural heritage.</p>
            
            <h3>🎮 Educational Games</h3>
            <p>Learn about Zimbabwe's wildlife through fun and interactive games!</p>
            <a href="/games" class="btn">🎯 Play Games</a>
            <a href="/games/animal-sounds" class="btn">🔊 Animal Sounds Quiz</a>
            
            <h3>🌿 Explore Nature</h3>
            <p>Discover Zimbabwe's rich biodiversity, from the iconic Baobab trees to diverse wildlife.</p>
            <a href="/trees" class="btn">🌳 Trees</a>
            <a href="/mammals" class="btn">🦁 Mammals</a>
            <a href="/birds" class="btn">🦅 Birds</a>
            
            <h3>🏞️ National Parks</h3>
            <p>Explore Zimbabwe's protected areas and conservation efforts.</p>
            <a href="/national-parks" class="btn">🏞️ National Parks</a>
            
            <hr style="margin: 30px 0;">
            <p><em>Created with ❤️ by Tonde Kawere to share Zimbabwe's natural wonders with the world.</em></p>
            <p><strong>Mission:</strong> To educate people about nature and promote conservation awareness.</p>
        </div>
    </body>
    </html>
    '''

@app.route('/games')
def games():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Educational Games - Nature Zimbabwe</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }
            .container { max-width: 800px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; }
            h1 { color: #2D5016; }
            .game-card { border: 2px solid #2D5016; padding: 20px; margin: 15px 0; border-radius: 10px; }
            .btn { background: #2D5016; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; display: inline-block; margin: 10px 5px; }
            .btn:hover { background: #4A7C59; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🎮 Educational Wildlife Games</h1>
            <p>Learn about Zimbabwe's wildlife through fun and interactive games created by Tonde!</p>
            
            <div class="game-card">
                <h3>🔊 Animal Sounds Quiz</h3>
                <p>Test your knowledge of Zimbabwe's wildlife! Listen to animal sounds and identify which animal makes each sound.</p>
                <a href="/games/animal-sounds" class="btn">Play Now</a>
            </div>
            
            <div class="game-card">
                <h3>🧠 Nature Trivia</h3>
                <p>Challenge yourself with questions about Zimbabwe's flora, fauna, and national parks.</p>
                <a href="/games/quiz" class="btn">Coming Soon</a>
            </div>
            
            <div class="game-card">
                <h3>🃏 Memory Match</h3>
                <p>Match pairs of animals, trees, and natural features from Zimbabwe.</p>
                <a href="/games/memory" class="btn">Coming Soon</a>
            </div>
            
            <a href="/" class="btn">🏠 Back to Home</a>
        </div>
    </body>
    </html>
    '''

@app.route('/games/animal-sounds')
def animal_sounds():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Zimbabwe Animal Sounds Quiz - Nature Zimbabwe</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; background: #f5f5f5; }
            .container { max-width: 800px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; }
            h1 { color: #2D5016; text-align: center; }
            .game-area { text-align: center; margin: 30px 0; }
            .btn { background: #2D5016; color: white; padding: 15px 30px; text-decoration: none; border-radius: 5px; display: inline-block; margin: 10px; border: none; cursor: pointer; font-size: 16px; }
            .btn:hover { background: #4A7C59; }
            .animal-options { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin: 20px 0; }
            .animal-btn { background: #4A7C59; padding: 15px; border-radius: 8px; }
            #sound-description { background: #e8f5e8; padding: 15px; border-radius: 5px; margin: 20px 0; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🔊 Zimbabwe Animal Sounds Quiz</h1>
            <p style="text-align: center;">Created by Tonde to help you learn about Zimbabwe's amazing wildlife!</p>
            
            <div class="game-area">
                <div id="sound-description">
                    <p>🎯 <strong>How to Play:</strong></p>
                    <p>1. Click "Play Sound" to hear an animal sound</p>
                    <p>2. Choose which animal you think makes that sound</p>
                    <p>3. Learn about Zimbabwe's incredible wildlife!</p>
                </div>
                
                <button class="btn" onclick="playRandomSound()">🔊 Play Sound</button>
                <button class="btn" onclick="testAudio()">🎵 Test Audio</button>
                
                <div class="animal-options">
                    <button class="animal-btn" onclick="selectAnimal('Lion')">🦁 Lion</button>
                    <button class="animal-btn" onclick="selectAnimal('Elephant')">🐘 Elephant</button>
                    <button class="animal-btn" onclick="selectAnimal('Hippo')">🦛 Hippo</button>
                    <button class="animal-btn" onclick="selectAnimal('Zebra')">🦓 Zebra</button>
                    <button class="animal-btn" onclick="selectAnimal('Hyena')">🐺 Hyena</button>
                    <button class="animal-btn" onclick="selectAnimal('African Fish Eagle')">🦅 Fish Eagle</button>
                </div>
                
                <div id="result" style="margin: 20px 0; font-size: 18px;"></div>
                
                <a href="/games" class="btn">🎮 Back to Games</a>
                <a href="/" class="btn">🏠 Home</a>
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
                
                // Try to play synthetic sound
                playSyntheticSound(currentAnimal.name);
            }
            
            function playSyntheticSound(animalName) {
                try {
                    const audioContext = new (window.AudioContext || window.webkitAudioContext)();
                    
                    if (audioContext.state === 'suspended') {
                        audioContext.resume();
                    }
                    
                    const oscillator = audioContext.createOscillator();
                    const gainNode = audioContext.createGain();
                    
                    oscillator.connect(gainNode);
                    gainNode.connect(audioContext.destination);
                    
                    // Different frequencies for different animals
                    let frequency = 440;
                    let duration = 1;
                    
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
                    document.getElementById('result').innerHTML = 
                        '<p style="color: orange;">🔊 Please play a sound first!</p>';
                    return;
                }
                
                const isCorrect = selectedAnimal === currentAnimal.name;
                const resultDiv = document.getElementById('result');
                
                if (isCorrect) {
                    resultDiv.innerHTML = 
                        '<p style="color: green;">🎉 Correct! That was a ' + currentAnimal.name + ' ' + currentAnimal.emoji + '</p>' +
                        '<p>' + currentAnimal.sound + '</p>';
                } else {
                    resultDiv.innerHTML = 
                        '<p style="color: red;">❌ Not quite! That was a ' + currentAnimal.name + ' ' + currentAnimal.emoji + '</p>' +
                        '<p>' + currentAnimal.sound + '</p>';
                }
                
                setTimeout(() => {
                    currentAnimal = null;
                    document.getElementById('sound-description').innerHTML = 
                        '<p>🎯 Ready for the next challenge? Click "Play Sound" to continue!</p>';
                }, 3000);
            }
        </script>
    </body>
    </html>
    '''

# API routes
@app.route('/api/test')
def api_test():
    return {'status': 'success', 'message': 'Nature Zimbabwe API is working!', 'creator': 'Tonde Kawere'}

@app.route('/debug')
def debug():
    return {
        'status': 'Flask app is running on Vercel',
        'creator': 'Tonde Kawere',
        'mission': 'To educate people about Zimbabwe nature',
        'routes': [str(rule) for rule in app.url_map.iter_rules()]
    }

# Placeholder routes for other pages
@app.route('/trees')
def trees():
    return '<h1>🌳 Trees of Zimbabwe</h1><p>Coming soon! Created by Tonde.</p><a href="/">Back to Home</a>'

@app.route('/mammals')
def mammals():
    return '<h1>🦁 Mammals of Zimbabwe</h1><p>Coming soon! Created by Tonde.</p><a href="/">Back to Home</a>'

@app.route('/birds')
def birds():
    return '<h1>🦅 Birds of Zimbabwe</h1><p>Coming soon! Created by Tonde.</p><a href="/">Back to Home</a>'

@app.route('/national-parks')
def national_parks():
    return '<h1>🏞️ Zimbabwe National Parks</h1><p>Coming soon! Created by Tonde.</p><a href="/">Back to Home</a>'

# This is crucial for Vercel
if __name__ == '__main__':
    app.run(debug=True)
