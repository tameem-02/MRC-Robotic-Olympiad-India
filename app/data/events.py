"""Event data for MRC Global Olympiad competitions"""

EVENTS_DATA = [
    # Marathon
    {
        'id': 1,
        'title': 'Marathon',
        'date': '2026-04-03',
        'location': 'Heraklion, Crete, Greece',
        'category': 'Endurance',
        'description': 'Robot marathon race requiring endurance, navigation, and consistent performance over long distances',
        'image': 'marathon.jpg',
        'video_url': 'https://www.youtube.com/embed/7mTL9O0d-Zc',
        'details': 'Robot marathon race requiring endurance, navigation, and consistent performance over long distances. Teams must program autonomous robots to complete multiple laps efficiently while managing power consumption and navigation accuracy.',
        'registration_open': True,
        'max_participants': 120,
        'duration': '30 minutes',
        'difficulty': 'Advanced',
        'team_size': '2-5 members',
        'fee': '€95 (Early) / €125 (Late)',
        'age_categories': [
            {'name': 'KIDS', 'age': '10 to 12 years old', 'level': 'Elementary School'},
            {'name': 'TEENS', 'age': '12+ to 15 years old', 'level': 'Middle School'},
            {'name': 'SENIOR', 'age': '15+ to 18 years old', 'level': 'High School'},
            {'name': 'ADULTS', 'age': '18+ years old', 'level': 'University/Adults'}
        ],
        'divisions': {
            'basic': {
                'title': 'Marathon Basic',
                'description': 'Robots built from educational modular kits with official hubs/controllers (e.g., LEGO® Education EV3/SPIKE/Robot Inventor, ZMROBO, MAKERZOID, ENJOY AI, Makeblock mBot, DFRobot Maqueen), or equivalent.'
            },
            'advanced': {
                'title': 'Marathon Advanced',
                'description': 'Robots built with general-purpose microcontrollers/electronics (e.g., Arduino, ESP32, STM32, Raspberry Pi, Teensy, NVIDIA Jetson, BeagleBone) and similar custom/open hardware.'
            }
        },
        'notes': [
            '🚨 Each age category competes separately.',
            '⚠️ The Adults age category does NOT compete in the Marathon Basic division.'
        ],
        'quick_guide': 'https://www.he-ro.gr/minoan-robotsports-competition',
        'practice_file': 'https://www.he-ro.gr/_files/ugd/75e4cb_af8241d0fdd5480787aa77940115e4ee.pdf'
    },
    
    # Archery
    {
        'id': 2,
        'title': 'Archery',
        'date': '2026-04-03',
        'location': 'Heraklion, Crete, Greece',
        'category': 'Precision',
        'description': 'Precision targeting competition where robots aim and launch projectiles at designated targets',
        'image': 'archery.jpg',
        'video_url': 'https://www.youtube.com/embed/dQw4w9WgXcQ',
        'details': 'Precision targeting competition where robots must aim and launch projectiles at designated targets with accuracy. Requires advanced sensors, precise mechanical design, and sophisticated aiming algorithms.',
        'registration_open': True,
        'max_participants': 80,
        'duration': '15 minutes',
        'difficulty': 'Intermediate',
        'team_size': '2-5 members',
        'fee': '€95 (Early) / €125 (Late)',
        'age_range': 'High School, University, Adults'
    },
    
    # Relay Race
    {
        'id': 3,
        'title': 'Relay Race',
        'date': '2026-04-03',
        'location': 'Heraklion, Crete, Greece',
        'category': 'Team Sport',
        'description': 'Team coordination challenge where multiple robots pass objects between stages',
        'image': 'relay.jpg',
        'video_url': 'https://www.youtube.com/embed/dQw4w9WgXcQ',
        'details': 'Team-based relay competition where multiple robots must coordinate to complete sequential tasks and pass objects between stages. Tests teamwork, timing, and inter-robot communication.',
        'registration_open': True,
        'max_participants': 100,
        'duration': '20 minutes',
        'difficulty': 'Intermediate',
        'team_size': '3-5 members',
        'fee': '€95 (Early) / €125 (Late)',
        'age_range': 'All Categories'
    },
    
    # Obstacle Race
    {
        'id': 4,
        'title': 'Obstacle Race',
        'date': '2026-04-03',
        'location': 'Heraklion, Crete, Greece',
        'category': 'Navigation',
        'description': 'Navigate complex terrain with climbing and maneuvering through challenging obstacle courses',
        'image': 'obstacle.jpg',
        'video_url': 'https://www.youtube.com/embed/dQw4w9WgXcQ',
        'details': 'Navigate through complex obstacle courses requiring climbing, traversing, and maneuvering capabilities. Tests robot mobility, balance, and autonomous navigation through challenging terrain.',
        'registration_open': True,
        'max_participants': 90,
        'duration': '10 minutes',
        'difficulty': 'Advanced',
        'team_size': '2-5 members',
        'fee': '€95 (Early) / €125 (Late)',
        'age_range': 'High School, University'
    },
    
    # Mountain Bike
    {
        'id': 5,
        'title': 'Mountain Bike',
        'date': '2026-04-03',
        'location': 'Heraklion, Crete, Greece',
        'category': 'Racing',
        'description': 'Off-road biking simulation requiring robust design and advanced control systems',
        'image': 'mountain.jpg',
        'video_url': 'https://www.youtube.com/embed/dQw4w9WgXcQ',
        'details': 'Off-road biking simulation with terrain challenges, requiring robust mechanical design, advanced control systems, and ability to handle variable terrain conditions.',
        'registration_open': True,
        'max_participants': 70,
        'duration': '15 minutes',
        'difficulty': 'Advanced',
        'team_size': '2-5 members',
        'fee': '€95 (Early) / €125 (Late)',
        'age_range': 'High School, University, Adults'
    },
    
    # Football
    {
        'id': 6,
        'title': 'Football',
        'date': '2026-04-03',
        'location': 'Heraklion, Crete, Greece',
        'category': 'Team Sport',
        'description': 'Autonomous robot soccer competition requiring strategy, ball control, and teamwork',
        'image': 'football.jpg',
        'video_url': 'https://www.youtube.com/embed/dQw4w9WgXcQ',
        'details': 'Autonomous robot soccer competition where teams program robots to play soccer. Requires strategy, ball control, teamwork, and real-time decision making.',
        'registration_open': True,
        'max_participants': 100,
        'duration': '2x10 minutes',
        'difficulty': 'Intermediate',
        'team_size': '3-5 members',
        'fee': '€95 (Early) / €125 (Late)',
        'age_range': 'All Categories'
    },
    
    # Rally
    {
        'id': 7,
        'title': 'Rally',
        'date': '2026-04-03',
        'location': 'Heraklion, Crete, Greece',
        'category': 'Racing',
        'description': 'High-speed racing through varied terrain and checkpoints',
        'image': 'rally.jpg',
        'video_url': 'https://www.youtube.com/embed/dQw4w9WgXcQ',
        'details': 'High-speed racing competition through varied terrain and checkpoints. Tests speed, control, navigation accuracy, and ability to handle dynamic racing conditions.',
        'registration_open': True,
        'max_participants': 80,
        'duration': '5 minutes',
        'difficulty': 'Advanced',
        'team_size': '2-5 members',
        'fee': '€95 (Early) / €125 (Late)',
        'age_range': 'High School, University'
    },
    
    # Shot Put
    {
        'id': 8,
        'title': 'Shot Put',
        'date': '2026-04-03',
        'location': 'Heraklion, Crete, Greece',
        'category': 'Power',
        'description': 'Projectile launching competition measuring distance and accuracy',
        'image': 'shotput.jpg',
        'video_url': 'https://www.youtube.com/embed/dQw4w9WgXcQ',
        'details': 'Projectile launching competition measuring distance and accuracy. Requires mechanical power, precision engineering, and optimal launch angle calculations.',
        'registration_open': True,
        'max_participants': 90,
        'duration': '3 attempts',
        'difficulty': 'Intermediate',
        'team_size': '2-5 members',
        'fee': '€95 (Early) / €125 (Late)',
        'age_range': 'All Categories'
    },
    
    # Exhibition
    {
        'id': 9,
        'title': 'Exhibition',
        'date': '2026-04-03',
        'location': 'Heraklion, Crete, Greece',
        'category': 'Creative',
        'description': 'Open category for creative robotics projects and innovative designs',
        'image': 'exhibition.jpg',
        'video_url': 'https://www.youtube.com/embed/dQw4w9WgXcQ',
        'details': 'Open category for creative robotics projects. Teams showcase innovative designs, performances, or demonstrations without strict competition rules. Perfect for unique and artistic robot presentations.',
        'registration_open': True,
        'max_participants': 120,
        'duration': '10 minutes',
        'difficulty': 'All Levels',
        'team_size': '2-5 members',
        'fee': '€95 (Early) / €125 (Late)',
        'age_range': 'All Categories'
    },
    
    # Water Polo
    {
        'id': 10,
        'title': 'Water Polo',
        'date': '2026-04-03',
        'location': 'Heraklion, Crete, Greece',
        'category': 'Aquatic',
        'description': 'Aquatic robotics combining swimming, ball handling, and goal scoring',
        'image': 'waterpolo.jpg',
        'video_url': 'https://www.youtube.com/embed/dQw4w9WgXcQ',
        'details': 'Aquatic robotics competition combining swimming, ball handling, and goal scoring in water environment. Tests waterproofing, buoyancy control, and aquatic locomotion.',
        'registration_open': True,
        'max_participants': 60,
        'duration': '2x8 minutes',
        'difficulty': 'Advanced',
        'team_size': '3-5 members',
        'fee': '€95 (Early) / €125 (Late)',
        'age_range': 'High School, University, Adults'
    },
    
    # Weightlifting
    {
        'id': 11,
        'title': 'Weightlifting',
        'date': '2026-04-03',
        'location': 'Heraklion, Crete, Greece',
        'category': 'Strength',
        'description': 'Strength competition where robots lift and move heavy objects',
        'image': 'weightlifting.jpg',
        'video_url': 'https://www.youtube.com/embed/dQw4w9WgXcQ',
        'details': 'Strength-based competition where robots must lift and move heavy objects. Tests mechanical power, stability, structural integrity, and efficient power transmission.',
        'registration_open': True,
        'max_participants': 80,
        'duration': '3 attempts',
        'difficulty': 'Intermediate',
        'team_size': '2-5 members',
        'fee': '€95 (Early) / €125 (Late)',
        'age_range': 'All Categories'
    },
    
    # Pentathlon Arena
    {
        'id': 12,
        'title': 'Pentathlon Arena',
        'date': '2026-04-03',
        'location': 'Heraklion, Crete, Greece',
        'category': 'Multi-Discipline',
        'description': 'Five disciplines in one event - ultimate test of robot versatility',
        'image': 'pentathlon.jpg',
        'video_url': 'https://www.youtube.com/embed/dQw4w9WgXcQ',
        'details': 'Five-discipline competition combining multiple challenges in one event. The most comprehensive test of robot versatility, team capability, and engineering excellence across diverse tasks.',
        'registration_open': True,
        'max_participants': 50,
        'duration': 'Full day',
        'difficulty': 'Expert',
        'team_size': '3-5 members',
        'fee': '€95 (Early) / €125 (Late)',
        'age_range': 'High School, University, Adults'
    },
    
    # Shooting
    {
        'id': 13,
        'title': 'Shooting',
        'date': '2026-04-03',
        'location': 'Heraklion, Crete, Greece',
        'category': 'Precision',
        'description': 'Target shooting requiring precision aiming and firing mechanisms',
        'image': 'shooting.jpg',
        'video_url': 'https://www.youtube.com/embed/dQw4w9WgXcQ',
        'details': 'Target shooting competition requiring precision aiming and firing mechanisms. Tests accuracy, sensor integration, targeting algorithms, and mechanical consistency.',
        'registration_open': True,
        'max_participants': 70,
        'duration': '10 shots',
        'difficulty': 'Intermediate',
        'team_size': '2-5 members',
        'fee': '€95 (Early) / €125 (Late)',
        'age_range': 'High School, University, Adults'
    },
    
    # Rowing
    {
        'id': 14,
        'title': 'Rowing',
        'date': '2026-04-03',
        'location': 'Heraklion, Crete, Greece',
        'category': 'Aquatic',
        'description': 'Water-based linear racing with synchronized mechanical rowing motion',
        'image': 'rowing.jpg',
        'video_url': 'https://www.youtube.com/embed/dQw4w9WgXcQ',
        'details': 'Water-based linear racing requiring synchronized mechanical rowing motion and straight-line navigation. Tests aquatic propulsion systems and directional stability.',
        'registration_open': True,
        'max_participants': 60,
        'duration': '5 minutes',
        'difficulty': 'Intermediate',
        'team_size': '2-5 members',
        'fee': '€95 (Early) / €125 (Late)',
        'age_range': 'All Categories'
    },
    
    # Curling
    {
        'id': 15,
        'title': 'Curling',
        'date': '2026-04-03',
        'location': 'Heraklion, Crete, Greece',
        'category': 'Precision',
        'description': 'Precision sliding sport with fine motor control and strategic stone placement',
        'image': 'curling.jpg',
        'video_url': 'https://www.youtube.com/embed/dQw4w9WgXcQ',
        'details': 'Precision sliding sport where robots must accurately deliver stones to target areas. Requires fine motor control, precise force application, and strategic planning.',
        'registration_open': True,
        'max_participants': 50,
        'duration': '8 ends',
        'difficulty': 'Advanced',
        'team_size': '2-4 members',
        'fee': '€95 (Early) / €125 (Late)',
        'age_range': 'High School, University, Adults'
    }
]


def get_all_events():
    """Return all MRC sports events"""
    return EVENTS_DATA


def get_event_by_id(event_id):
    """Return a specific event by ID"""
    for event in EVENTS_DATA:
        if event['id'] == event_id:
            return event
    return None


def get_events_by_category(category):
    """Return events filtered by category"""
    return [event for event in EVENTS_DATA if event['category'] == category]


def get_upcoming_events():
    """Return upcoming events (registration open)"""
    return [event for event in EVENTS_DATA if event['registration_open']]


def get_endurance_sports():
    """Return endurance-based sports"""
    return [event for event in EVENTS_DATA if event['category'] == 'Endurance']


def get_precision_sports():
    """Return precision-based sports"""
    return [event for event in EVENTS_DATA if event['category'] == 'Precision']


def get_team_sports():
    """Return team-based sports"""
    return [event for event in EVENTS_DATA if event['category'] == 'Team Sport']
