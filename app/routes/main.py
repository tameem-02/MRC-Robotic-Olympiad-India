from flask import Blueprint, render_template

main = Blueprint('main', __name__)

# Basic Pages
@main.route('/')
def home():
    return render_template('pages/home.html')

@main.route('/profile')
def profile():
    return render_template('pages/profile.html')

@main.route('/about')
def about():
    return render_template('pages/about.html')

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

# MRC Olympiad Main Page
@main.route('/mrc-olympiad')
def mrc_olympiad():
    """MRC Olympiad main page with all sports cards"""
    return render_template('pages/mrc_olympiad.html')

# MRC Competition Individual Pages
@main.route('/mrc-competitions/marathon')
def mrc_marathon():
    return render_template('pages/mrc_competitions/marathon.html')

@main.route('/mrc-competitions/archery')
def mrc_archery():
    return render_template('pages/mrc_competitions/archery.html')

@main.route('/mrc-competitions/relay-race')
def mrc_relay_race():
    return render_template('pages/mrc_competitions/relay_race.html')

@main.route('/mrc-competitions/obstacle-race')
def mrc_obstacle_race():
    return render_template('pages/mrc_competitions/obstacle_race.html')

@main.route('/mrc-competitions/mountain-bike')
def mrc_mountain_bike():
    return render_template('pages/mrc_competitions/mountain_bike.html')

@main.route('/mrc-competitions/football')
def mrc_football():
    return render_template('pages/mrc_competitions/football.html')

@main.route('/mrc-competitions/rally')
def mrc_rally():
    return render_template('pages/mrc_competitions/rally.html')

@main.route('/mrc-competitions/shot-put')
def mrc_shot_put():
    return render_template('pages/mrc_competitions/shot_put.html')

@main.route('/mrc-competitions/exhibition')
def mrc_exhibition():
    return render_template('pages/mrc_competitions/exhibition.html')

@main.route('/mrc-competitions/water-polo')
def mrc_water_polo():
    return render_template('pages/mrc_competitions/water_polo.html')

@main.route('/mrc-competitions/weightlifting')
def mrc_weightlifting():
    return render_template('pages/mrc_competitions/weightlifting.html')

@main.route('/mrc-competitions/pentathlon')
def mrc_pentathlon():
    return render_template('pages/mrc_competitions/pentathlon.html')

@main.route('/mrc-competitions/shooting')
def mrc_shooting():
    return render_template('pages/mrc_competitions/shooting.html')

@main.route('/mrc-competitions/rowing')
def mrc_rowing():
    return render_template('pages/mrc_competitions/rowing.html')

@main.route('/mrc-competitions/curling')
def mrc_curling():
    return render_template('pages/mrc_competitions/curling.html')


# New MRC Competition Routes
@main.route('/mrc-olympiad/drones')
def mrc_drones():
    return render_template('pages/mrc_competitions/drones.html')

@main.route('/mrc-olympiad/drones-soccer')
def mrc_drones_soccer():
    return render_template('pages/mrc_competitions/drones_soccer.html')

@main.route('/mrc-olympiad/weightlifting-humanoid')
def mrc_weightlifting_humanoid():
    return render_template('pages/mrc_competitions/weightlifting_humanoid.html')

@main.route('/mrc-olympiad/humanoid-obstacle')
def mrc_humanoid_obstacle():
    return render_template('pages/mrc_competitions/humanoid_obstacle.html')

@main.route('/mrc-olympiad/wrestling-humanoid')
def mrc_wrestling_humanoid():
    return render_template('pages/mrc_competitions/wrestling_humanoid.html')

@main.route('/mrc-olympiad/wrestling-cage-500')
def mrc_wrestling_cage_500():
    return render_template('pages/mrc_competitions/wrestling_cage_500.html')

@main.route('/mrc-olympiad/wrestling-cage-1500')
def mrc_wrestling_cage_1500():
    return render_template('pages/mrc_competitions/wrestling_cage_1500.html')

@main.route('/mrc-olympiad/wrestling-mega')
def mrc_wrestling_mega():
    return render_template('pages/mrc_competitions/wrestling_mega.html')

@main.route('/mrc-olympiad/wrestling-classic')
def mrc_wrestling_classic():
    return render_template('pages/mrc_competitions/wrestling_classic.html')

@main.route('/mrc-olympiad/wrestling-mini')
def mrc_wrestling_mini():
    return render_template('pages/mrc_competitions/wrestling_mini.html')

@main.route('/mrc-olympiad/wrestling-micro')
def mrc_wrestling_micro():
    return render_template('pages/mrc_competitions/wrestling_micro.html')

@main.route('/mrc-olympiad/wrestling-nano')
def mrc_wrestling_nano():
    return render_template('pages/mrc_competitions/wrestling_nano.html')

@main.route('/mrc-olympiad/marathon-turbo')
def mrc_marathon_turbo():
    return render_template('pages/mrc_competitions/marathon_turbo.html')

@main.route('/mrc-olympiad/hockey')
def mrc_hockey():
    return render_template('pages/mrc_competitions/hockey.html')

@main.route('/mrc-olympiad/bowling')
def mrc_bowling():
    return render_template('pages/mrc_competitions/bowling.html')

