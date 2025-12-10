from flask import Blueprint, render_template, redirect, url_for, jsonify
import requests
import json

main = Blueprint('main', __name__)

# ------------------------
# HELPER FUNCTIONS
# ------------------------

def create_empty_counts():
    """Return default counts for all competitions."""
    return {
        "MARATHON": 0,
        "ARCHERY": 0,
        "RELAY RACE": 0,
        "OBSTACLE RACE": 0,
        "MOUNTAIN BIKE": 0,
        "FOOTBALL": 0,
        "RALLY": 0,
        "SHOT PUT": 0,
        "EXHIBITION": 0,
        "WATER POLO": 0,
        "WEIGHTLIFTING DIY ROBOTS": 0,
        "PENTATHLON ARENA": 0,
        "SHOOTING": 0,
        "ROWING": 0,
        "GIRLING": 0,
        "DRONES": 0,
        "DRONES SOCCER": 0,
        "WEIGHTLIFTING HUMANOID": 0,
        "HUMANOID OBSTACLE RACE": 0,
        "WRESTLING HUMANOID": 0,
        "WRESTLING GAGE 500gr": 0,
        "WRESTLING GAGE 1.5KG": 0,
        "WRESTLING MEGA": 0,
        "WRESTLING CLASSIC": 0,
        "WRESTLING MINI": 0,
        "WRESTLING MICRO": 0,
        "WRESTLING NANO": 0,
        "MARATHON TURBO": 0,
        "HOCKEY": 0,
        "BOWLING": 0
    }

# ------------------------
# BASIC PAGES
# ------------------------

@main.route('/')
def home():
    return render_template('pages/home.html')

@main.route('/profile')
def profile():
    return render_template('pages/profile.html')

@main.route('/about')
def about():
    return render_template('pages/about.html')  # fixed

@main.route('/register')
def register():
    return render_template('pages/register.html')

@main.route('/register/<competition>')
def competition_register(competition):
    gscript_url = "https://script.google.com/macros/s/AKfycbyx8jwZm0SLvXbdorykwOFSBwOKOIfbYB1vwpgcbbTT3tEJFVDucfklNQRDUbPGNCTI/exec"
    return redirect(f"{gscript_url}?competition={competition}")

@main.route('/contact')
def contact():
    return render_template('pages/contact.html')

@main.route('/events')
def events():
    return render_template('pages/events.html')

@main.route('/partnerships')
def partnerships():
    return render_template('pages/partnerships.html')

@main.route('/resources')
def resources():
    return render_template('pages/resources.html')

@main.route('/gallery')
def gallery():
    return render_template('pages/gallery.html')

@main.route('/news')
def news():
    return render_template('pages/news.html')

@main.route('/faq')
def faq():
    return render_template('pages/faq.html')

# ------------------------
# MRC OLYMPIAD MAIN
# ------------------------

@main.route('/mrc-olympiad')
def mrc_olympiad():
    return render_template('pages/mrc_olympiad.html')

# ------------------------
# MRC COMPETITION ROUTES
# ------------------------

competition_pages = [
    "marathon", "archery", "relay_race", "obstacle_race", "mountain_bike",
    "football", "rally", "shot_put", "exhibition", "water_polo",
    "weightlifting", "pentathlon", "shooting", "rowing", "curling"
]

for comp in competition_pages:
    route = f"/mrc-competitions/{comp.replace('_', '-')}"
    template = f"pages/mrc_competitions/{comp}.html"
    main.add_url_rule(route, comp, lambda template=template: render_template(template))

# ------------------------
# NEW MRC OLYMPIAD ROUTES
# ------------------------

olympiad_pages = [
    "drones", "drones_soccer", "weightlifting_humanoid", "humanoid_obstacle",
    "wrestling_humanoid", "wrestling_cage_500", "wrestling_cage_1500",
    "wrestling_mega", "wrestling_classic", "wrestling_mini",
    "wrestling_micro", "wrestling_nano", "marathon_turbo",
    "hockey", "bowling"
]

for comp in olympiad_pages:
    route = f"/mrc-olympiad/{comp.replace('_', '-')}"
    template = f"pages/mrc_competitions/{comp}.html"
    main.add_url_rule(route, comp, lambda template=template: render_template(template))

# ------------------------
# API ROUTES
# ------------------------

@main.route('/api/counts')
def get_counts_api():
    try:
        gscript_url = "https://script.google.com/macros/s/AKfycbyx8jwZm0SLvXbdorykwOFSBwOKOIfbYB1vwpgcbbTT3tEJFVDucfklNQRDUbPGNCTI/exec"
        params = {'action': 'getCounts'}
        response = requests.get(gscript_url, params=params, timeout=10)
        response.raise_for_status()

        try:
            data = response.json()
            return jsonify(data)
        except json.JSONDecodeError:
            return jsonify({
                'counts': create_empty_counts(),
                'error': 'Invalid JSON response from Google Apps Script',
                'raw_preview': response.text[:500] if len(response.text) > 0 else 'Empty response'
            })

    except requests.exceptions.Timeout:
        return jsonify({
            'counts': create_empty_counts(),
            'error': 'Request timeout'
        })

    except requests.exceptions.RequestException as e:
        return jsonify({
            'counts': create_empty_counts(),
            'error': 'Network error',
            'message': str(e)
        })

    except Exception as e:
        return jsonify({
            'counts': create_empty_counts(),
            'error': 'Server error',
            'message': str(e)
        })

@main.route('/api/test')
def test_api():
    return jsonify({
        'message': 'API is working',
        'status': 'success',
        'timestamp': '2025-12-10T12:00:00Z'
    })
