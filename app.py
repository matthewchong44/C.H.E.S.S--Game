#!/usr/bin/env python
from threading import Lock
from flask import Flask, render_template, session, request, \
    copy_current_request_context,request,jsonify
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect
import sys
import json
# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
async_mode = None

app = Flask(__name__, static_folder='public', static_url_path='')
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()


def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        socketio.sleep(10)
        count += 1
        socketio.emit('my_response',
                      {'data': 'Server generated event', 'count': count},
                      namespace='/test')


@app.route('/')
def index():
    return render_template('menu.html', async_mode=socketio.async_mode)

app.route('/index')
def game(name):
    return render_template('index.html')


# Handle any unhandled filename by loading its template
@app.route('/<name>')
def generic(name):
    if name == "index":
        global numberofplayer
        if numberofplayer<2:
            numberofplayer+=1
            print("--------------------------------")
            print(numberofplayer)
            return render_template(name + '.html')
        else:
            return render_template('cannotplay.html')
    else:
        return render_template(name+'.html')

# @socketio.on('my_event', namespace='/test')
# def test_message(message):
#     session['receive_count'] = session.get('receive_count', 0) + 1
#     emit('my_response1',
#          {'data': message['data'], 'count': session['receive_count']})


# @socketio.on('my_broadcast_event', namespace='/test')
# def test_broadcast_message(message):
#     session['receive_count'] = session.get('receive_count', 0) + 1
#     emit('my_response1',
#          {'data': message['data'], 'count': session['receive_count']},
#          broadcast=True)


@socketio.on('join', namespace='/test')
def join(message):
    #global numberofplayer
    #print(numberofplayer)
    #f numberofplayer <2:
     #   numberofplayer+=1
    join_room(message['room'])
    session['receive_count'] = session.get('receive_count', 0) + 1
    #print("djsfkahfjdak----------")
    
        
    emit('my_response',
        {'data': 'In rooms: ' + ', '.join(rooms()),
        'count': session['receive_count']})


# @socketio.on('leave', namespace='/test')
# def leave(message):
#     leave_room(message['room'])
#     session['receive_count'] = session.get('receive_count', 0) + 1
#     emit('my_response1',
#          {'data': 'In rooms: ' + ', '.join(rooms()),
#           'count': session['receive_count']})


# @socketio.on('close_room', namespace='/test')
# def close(message):
#     session['receive_count'] = session.get('receive_count', 0) + 1
#     emit('my_response1', {'data': 'Room ' + message['room'] + ' is closing.',
#                          'count': session['receive_count']},
#         room=message['room'])
#     close_room(message['room'])

@socketio.on('my_room_event', namespace='/test')
def send_room_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    #print(message['data'])
    emit('my_response1',
         {'data': message['data'], 'count': session['receive_count']},
         room=message['room'])


# @socketio.on('disconnect_request', namespace='/test')
# def disconnect_request():
#     @copy_current_request_context
#     def can_disconnect():
#         disconnect()

#     session['receive_count'] = session.get('receive_count', 0) + 1
#     # for this emit we use a callback function
#     # when the callback function is invoked we know that the message has been
#     # received and it is safe to disconnect
#     emit('my_response1',
#          {'data': 'Disconnected!', 'count': session['receive_count']},
#          callback=can_disconnect)

@socketio.on('senddata', namespace='/test')
def senddata():                     #USELESS
    return "RETURN"
    


@socketio.on('my_ping', namespace='/test')
def ping_pong():
    emit('my_pong')
    
@app.route('/postmethod', methods = ['POST'])
def get_post_javascript_data():
    if request.method == "POST":
        jsdata = json.loads(request.form['javascript_data'])#request.form['javascript_data']
    gamepiece = jsdata[0]['piece']
    current_loc = jsdata[0]['current_loc']
    new_loc = jsdata[0]['new_loc']
    return jsonify(gamepiece,current_loc,new_loc)
    #return emit('broadcast', 'hello friends!');


#need a method to broadcast info


# @socketio.on('connect', namespace='/test')
# def test_connect():
#     global thread
#     with thread_lock:
#         if thread is None:
#             thread = socketio.start_background_task(background_thread)
#     emit('my_response1', {'data': 'Connected', 'count': 0})


# @socketio.on('disconnect', namespace='/test')
# def test_disconnect():
#     print('Client disconnected', request.sid)


if __name__ == '__main__':
    numberofplayer=0
    socketio.run(app, debug=True)
