from flask import Flask, g, jsonify, request, redirect, render_template
from flask_socketio import SocketIO, emit


app = Flask(__name__)
socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")


@app.route('/display', methods=['GET'])
def display():
    return render_template('display.html')


@app.route('/scan', methods=['GET'])
def scan_qr():
    return render_template('scan.html')


@app.route('/connect-display/<string:peer_id>')
def page(peer_id):
    return render_template('share-screen.html', PeerDesktopID=peer_id)


@app.route('/ws')
def socket():
    return render_template('connect.html')

@socketio.on('connect')
def test_connect():
    emit('after connect',  {'data':'Lets dance'})



        
if __name__ == '__main__':
    socketio.run(app)
