from flask import render_template, request, jsonify
from app import app, db
from app.models import Message

@app.route('/')
def index():
    messages = Message.query.order_by(Message.timestamp.asc()).all()
    return render_template('index.html', messages=messages)

@app.route('/messages', methods=['GET'])
def get_messages():
    messages = Message.query.order_by(Message.timestamp.asc()).all()
    return jsonify([{'username': m.username, 'message': m.message, 'timestamp': m.timestamp.isoformat()} for m in messages])
