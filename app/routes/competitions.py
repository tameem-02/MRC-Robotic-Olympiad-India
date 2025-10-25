from flask import Blueprint, render_template, abort
from app.data.events import get_all_events, get_event_by_id

competitions_bp = Blueprint('competitions', __name__)

@competitions_bp.route('/')
def competitions_list():
    """Competitions listing page"""
    events = get_all_events()
    return render_template('pages/competitions.html', events=events)

@competitions_bp.route('/<int:event_id>')
def event_detail(event_id):
    """Event detail page"""
    event = get_event_by_id(event_id)
    if event is None:
        abort(404)
    return render_template('pages/event_detail.html', event=event)
