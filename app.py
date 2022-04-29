from flask import Flask, request, jsonify, render_template, send_file
import speech_to_text
import summarizer


app = Flask(__name__)


@app.route("/summarize", methods=["POST"])
def summarize():

    # get audio file
    audio_file = request.files["UploadedAudio"]

    # invoke the genre recognition service
    speech_to_text.s2t(audio_file)

    # make prediction
    summarized_text = summarizer.summarise("sample.txt")

    with open("output.txt", "w") as f:
        summarized_text = f.write(summarized_text)

    button = '<a href="/download" class="btn btn-dark btn-lg mt-3">Download Text File</a>'

    return render_template("index.html", button=button)


@app.route("/download")
def download():
    file = "output.txt"

    return send_file(file, as_attachment=True)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
