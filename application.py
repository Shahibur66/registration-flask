
from flask import Flask, render_template, request,redirect
import sqlite3


connect=sqlite3.connect('lecture2.db', check_same_thread=False)
cursor=connect.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS users(id INT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255))')
# cursor.execute("INSERT INTO user(name,email) VALUES('alice','alice@example.com')")
# cursor.execute("INSERT INTO user(name,email) VALUES('bob','bob@example.com')")
# connect.commit()
# cursor.close()
# connect.close()

app=Flask(__name__)

@app.route("/")
def index():
	rows=cursor.execute("SELECT * FROM users")
	print(rows)
	return render_template("index.html",rows=rows)

@app.route("/register",methods=["GET","POST"])
def register():
	if request.method=="GET":
		return render_template("register.html")
	else:
		name=request.form.get("name")
		if not name:
			return render_template("apology.html",message="You must provide a name.")
		email=request.form.get("email")
		if not email:
			return render_template("apology.html",message="You must provide a email.")

		cursor.execute("INSERT INTO users(name,email) VALUES(?,?)",(name,email))
		connect.commit()
		return redirect("/")

@app.route("/delete")
def delete():
	cursor.execute("delete FROM users")
	connect.commit()
	return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)