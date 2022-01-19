import os
#import magic
import urllib.request
from app import app
from flask import Flask, flash, request, redirect, send_file, render_template
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	
@app.route('/')
def upload_form():
	return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_file():
	if request.method == 'POST':
        # check if the post request has the files part
		if 'files[]' not in request.files:
			flash('No file part')
			return redirect(request.url)
		files = request.files.getlist('files[]')
		for file in files:
			if file and allowed_file(file.filename):
				filename = secure_filename(file.filename)
				file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		flash('File(s) successfully uploaded')
		return redirect('/')

@app.route('/download', methods=['GET'])
def download():
   # import pdb; pdb.set_trace()
   # for file in path
   files = [f for f in os.listdir('.') if os.path.isfile(f)]
   file_names = []
   for f in files:
   	   file_names.append(f)
   if request.method == 'GET':
        # check if the post request has the files part
        # if 'files[]' not in request.files:
        # 	flash('No file part')
        # 	return redirect(request.url)
        # files = request.files.getlist('files[]')
        for filename in file_names:
        	# if file and allowed_file(file.filename):
        		# filename = secure_filename(file.filename)
        		return send_file(filename, as_attachment=True)
        flash('File successfully downloaded')
        return redirect('/')
   # return send_file('byte-of-python.pdf', as_attachment=True)


if __name__ == "__main__":
    app.run()