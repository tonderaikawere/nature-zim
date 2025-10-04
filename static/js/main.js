// Nature Zimbabwe - Main JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Initialize popovers
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Add fade-in animation to cards on scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
            }
        });
    }, observerOptions);

    // Observe all cards
    document.querySelectorAll('.nature-card, .game-card, .tool-card').forEach(card => {
        observer.observe(card);
    });

    // Back to top button
    const backToTopButton = createBackToTopButton();
    document.body.appendChild(backToTopButton);

    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 300) {
            backToTopButton.style.display = 'block';
        } else {
            backToTopButton.style.display = 'none';
        }
    });

    // Search functionality
    initializeSearch();

    // Theme toggle (if needed)
    initializeThemeToggle();

    // Initialize Quick Access
    initializeQuickAccess();
});

// Create back to top button
function createBackToTopButton() {
    const button = document.createElement('button');
    button.innerHTML = '<i class="fas fa-arrow-up"></i>';
    button.className = 'btn btn-nature position-fixed';
    button.style.cssText = `
        bottom: 20px;
        right: 20px;
        z-index: 1000;
        display: none;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    `;
    
    button.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
    
    return button;
}

// Initialize search functionality
function initializeSearch() {
    const searchInput = document.getElementById('siteSearch');
    if (searchInput) {
        searchInput.addEventListener('input', function(e) {
            const query = e.target.value.toLowerCase();
            performSearch(query);
        });
    }
}

// Perform site search
function performSearch(query) {
    if (query.length < 2) return;
    
    // This is a simple client-side search
    // In a real application, you might want to implement server-side search
    const searchableElements = document.querySelectorAll('[data-searchable]');
    
    searchableElements.forEach(element => {
        const text = element.textContent.toLowerCase();
        const parent = element.closest('.nature-card, .game-card, .tool-card');
        
        if (text.includes(query)) {
            if (parent) parent.style.display = 'block';
        } else {
            if (parent) parent.style.display = 'none';
        }
    });
}

// Theme toggle functionality
function initializeThemeToggle() {
    const themeToggle = document.getElementById('themeToggle');
    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            document.body.classList.toggle('dark-theme');
            localStorage.setItem('theme', document.body.classList.contains('dark-theme') ? 'dark' : 'light');
        });

        // Load saved theme
        const savedTheme = localStorage.getItem('theme');
        if (savedTheme === 'dark') {
            document.body.classList.add('dark-theme');
        }
    }
}

// Utility functions for games and tools
const NatureUtils = {
    // Random number generator
    random: (min, max) => Math.floor(Math.random() * (max - min + 1)) + min,
    
    // Shuffle array
    shuffle: (array) => {
        const newArray = [...array];
        for (let i = newArray.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [newArray[i], newArray[j]] = [newArray[j], newArray[i]];
        }
        return newArray;
    },
    
    // Format time
    formatTime: (seconds) => {
        const mins = Math.floor(seconds / 60);
        const secs = seconds % 60;
        return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
    },
    
    // Show notification
    showNotification: (message, type = 'success') => {
        const notification = document.createElement('div');
        notification.className = `alert alert-${type} position-fixed`;
        notification.style.cssText = `
            top: 20px;
            right: 20px;
            z-index: 9999;
            min-width: 300px;
        `;
        notification.textContent = message;
        
        document.body.appendChild(notification);
        
        setTimeout(() => {
            notification.remove();
        }, 3000);
    },
    
    // Local storage helpers
    saveToStorage: (key, data) => {
        try {
            localStorage.setItem(key, JSON.stringify(data));
        } catch (e) {
            console.error('Failed to save to localStorage:', e);
        }
    },
    
    loadFromStorage: (key, defaultValue = null) => {
        try {
            const data = localStorage.getItem(key);
            return data ? JSON.parse(data) : defaultValue;
        } catch (e) {
            console.error('Failed to load from localStorage:', e);
            return defaultValue;
        }
    }
};

// Game-specific utilities
const GameUtils = {
    // Score management
    saveScore: (game, score) => {
        const scores = NatureUtils.loadFromStorage('gameScores', {});
        if (!scores[game]) scores[game] = [];
        scores[game].push({
            score: score,
            date: new Date().toISOString(),
            timestamp: Date.now()
        });
        // Keep only top 10 scores
        scores[game].sort((a, b) => b.score - a.score);
        scores[game] = scores[game].slice(0, 10);
        NatureUtils.saveToStorage('gameScores', scores);
    },
    
    getHighScores: (game) => {
        const scores = NatureUtils.loadFromStorage('gameScores', {});
        return scores[game] || [];
    },
    
    // Timer functionality
    createTimer: (callback, interval = 1000) => {
        let seconds = 0;
        let isRunning = false;
        let intervalId;
        
        return {
            start: () => {
                if (!isRunning) {
                    isRunning = true;
                    intervalId = setInterval(() => {
                        seconds++;
                        callback(seconds);
                    }, interval);
                }
            },
            stop: () => {
                isRunning = false;
                if (intervalId) clearInterval(intervalId);
            },
            reset: () => {
                seconds = 0;
                callback(seconds);
            },
            getTime: () => seconds
        };
    }
};

// Tool-specific utilities
const ToolUtils = {
    // Calculator functions
    calculate: (expression) => {
        try {
            // Basic security: only allow numbers and basic operators
            if (!/^[0-9+\-*/().\s]+$/.test(expression)) {
                throw new Error('Invalid characters in expression');
            }
            return Function('"use strict"; return (' + expression + ')')();
        } catch (e) {
            return 'Error';
        }
    },
    
    // Unit conversions
    convertTemperature: (value, from, to) => {
        // Convert to Celsius first
        let celsius;
        switch (from.toLowerCase()) {
            case 'fahrenheit':
                celsius = (value - 32) * 5/9;
                break;
            case 'kelvin':
                celsius = value - 273.15;
                break;
            default:
                celsius = value;
        }
        
        // Convert from Celsius to target
        switch (to.toLowerCase()) {
            case 'fahrenheit':
                return celsius * 9/5 + 32;
            case 'kelvin':
                return celsius + 273.15;
            default:
                return celsius;
        }
    },
    
    convertLength: (value, from, to) => {
        const meters = {
            'mm': value / 1000,
            'cm': value / 100,
            'm': value,
            'km': value * 1000,
            'inch': value * 0.0254,
            'ft': value * 0.3048,
            'yard': value * 0.9144,
            'mile': value * 1609.34
        };
        
        const valueInMeters = meters[from] || value;
        
        const conversions = {
            'mm': valueInMeters * 1000,
            'cm': valueInMeters * 100,
            'm': valueInMeters,
            'km': valueInMeters / 1000,
            'inch': valueInMeters / 0.0254,
            'ft': valueInMeters / 0.3048,
            'yard': valueInMeters / 0.9144,
            'mile': valueInMeters / 1609.34
        };
        
        return conversions[to] || valueInMeters;
    },
    
    // BMI Calculator
    calculateBMI: (weight, height, weightUnit = 'kg', heightUnit = 'm') => {
        // Convert to kg and meters
        let weightKg = weight;
        let heightM = height;
        
        if (weightUnit === 'lbs') {
            weightKg = weight * 0.453592;
        }
        
        if (heightUnit === 'cm') {
            heightM = height / 100;
        } else if (heightUnit === 'ft') {
            heightM = height * 0.3048;
        }
        
        const bmi = weightKg / (heightM * heightM);
        
        let category;
        if (bmi < 18.5) category = 'Underweight';
        else if (bmi < 25) category = 'Normal weight';
        else if (bmi < 30) category = 'Overweight';
        else category = 'Obese';
        
        return {
            bmi: Math.round(bmi * 10) / 10,
            category: category
        };
    }
};

// Quick Access functionality
function initializeQuickAccess() {
    const quickAccessItems = document.querySelectorAll('.quick-access-item');
    
    quickAccessItems.forEach(item => {
        item.addEventListener('click', function(e) {
            e.preventDefault();
            const target = this.getAttribute('href') || this.dataset.target;
            
            if (target) {
                // Add loading state
                this.classList.add('loading');
                
                // Navigate to target
                if (target.startsWith('#')) {
                    // Scroll to section
                    const targetElement = document.querySelector(target);
                    if (targetElement) {
                        targetElement.scrollIntoView({
                            behavior: 'smooth',
                            block: 'start'
                        });
                    }
                } else {
                    // Navigate to page
                    window.location.href = target;
                }
                
                // Remove loading state after delay
                setTimeout(() => {
                    this.classList.remove('loading');
                }, 1000);
            }
        });
        
        // Add hover effects
        item.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-3px)';
        });
        
        item.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
}

// Export utilities for use in other scripts
window.NatureUtils = NatureUtils;
window.GameUtils = GameUtils;
window.ToolUtils = ToolUtils;
