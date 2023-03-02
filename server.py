from flask import Flask , render_template , request , redirect
import os 
import csv

app = Flask(__name__)


@app.route('/')
def my_home( ):
	return render_template("index.html")
'''
@app.route('/index.html')
def home( ):
	return render_template("index.html")

@app.route('/works.html')
def works( ):
	return render_template("works.html")

@app.route('/about.html')
def about( ):
	return render_template("about.html")

@app.route('/contact.html')
def contact( ):
	return render_template("contact.html")
'''

def write_data(data):
	email = data["email"]
	subject = data["subject"]
	message = data["message"]
	text = f"{email} , {subject} , {message} \n"
	if not os.path.exists("./database.csv") :
		with open("./database.txt" , 'w') as file:
			file.write(text)
	else:
		with open("./database.txt" , 'a') as file:
			file.write(text)


def write_data_csv(data):
	csv_header = ["email" , "subject" , "message"]
	row = [data["email"] , data["subject"] , data["message"]]
	if not os.path.exists("./database.csv") :
		with open("./database.csv" , 'w') as csvfile:
			writer = csv.writer(csvfile)
			writer.writerow(csv_header)
			writer.writerow(row) 
	else:
		with open("./database.csv" , 'a') as csvfile:
			writer = csv.writer(csvfile)
			writer.writerow(row)



@app.route('/<pagename>')
def page(pagename ):
	return render_template(pagename)


@app.route('/submit_form' , methods=["POST" , "GET"])
def submit_form( ):
	if request.method == "POST" :
		data = request.form.to_dict()
		print(data)
		write_data(data)
		write_data_csv(data)
		return redirect("/thankyou.html")
	else:
		return "Something went wrong, Please try again"


'''
@app.route('/<username>/<int:post_id>')
def hello_world(username , post_id):
	return render_template("index.html" , name = username , post_id = post_id)

@app.route('/about')
def blog():
	return render_template("about.html")

#@app.route('/favicon.ico')
#def blog():
#	return render_template("about.html")

'''