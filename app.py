from flask import Flask, request, render_template
from your_module import summarize, save_uploadedfile

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            file_path = save_uploadedfile(uploaded_file)
            summary_result = summarize(file_path)
            return render_template('result.html', file_path=file_path, summary_result=summary_result)
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
