from flask import Flask, render_template, request, send_from_directory
from flask_socketio import SocketIO, emit
from processor import VideoProcessor
import os
import threading

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-123')
socketio = SocketIO(app, cors_allowed_origins="*")

# Initialize processor
processor = VideoProcessor('input_videos', 'output_videos')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/image')
def serve_image():
    return send_from_directory('static', 'messi.jpg')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return {'status': 'error', 'message': 'No file uploaded'}, 400
    
    file = request.files['file']
    if file.filename == '':
        return {'status': 'error', 'message': 'No selected file'}, 400

    try:
        # Save file
        input_path = os.path.join(processor.input_dir, file.filename)
        file.save(input_path)

        # Start processing in background
        def process_task():
            try:
                # Call external processing script
                output_filename = processor.generate_filename(file.filename)
                exit_code = os.system(f"python main.py {input_path} {output_filename}")
                
                if exit_code == 0:
                    socketio.emit('processing_complete', {
                        'status': 'success',
                        'filename': output_filename
                    })
                else:
                    socketio.emit('processing_complete', {
                        'status': 'error',
                        'message': 'Processing failed'
                    })

            except Exception as e:
                socketio.emit('processing_complete', {
                    'status': 'error',
                    'message': str(e)
                })

        threading.Thread(target=process_task).start()

        return {'status': 'success', 'message': 'Processing started'}, 200

    except Exception as e:
        return {'status': 'error', 'message': str(e)}, 500

@app.route('/output/<filename>')
def serve_output(filename):
    return send_from_directory(processor.output_dir, filename)

@app.route('/latest-output')
def get_latest_output():
    latest = processor.get_latest_output()
    return {'filename': os.path.basename(latest)} if latest else {'error': 'No files'}, 200

if __name__ == '__main__':
    socketio.run(app, debug=True, port=5000)