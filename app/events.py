from flask_socketio import emit, join_room, leave_room
from app import socketio, db
from app.models import Message
from datetime import datetime

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('send_message')
def handle_message(data):
    username = data.get('username', 'Anonymous')
    message_text = data.get('message', '')
    
    if message_text:
        message = Message(username=username, message=message_text)
        db.session.add(message)
        db.session.commit()
        
        emit('receive_message', {
            'username': username,
            'message': message_text,
            'timestamp': datetime.utcnow().isoformat()
        }, broadcast=True)
