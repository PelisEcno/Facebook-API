from flask import Flask, request, jsonify
import yt_dlp

app = Flask(__name__)

@app.route('/get_video', methods=['GET'])
def get_video():
    url = request.args.get('url')

    if not url:
        return jsonify({"error": "Falta la URL"}), 400

    opciones = {
        'quiet': True,
        'format': 'best'
    }

    try:
        with yt_dlp.YoutubeDL(opciones) as ydl:
            info = ydl.extract_info(url, download=False)
            video_url = info.get('url', None)

        if video_url:
            return jsonify({"video_url": video_url})
        else:
            return jsonify({"error": "No se pudo obtener la URL del video"}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)