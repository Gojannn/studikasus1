import os

# import SQL untuk menggunakan bahasa SQL dalam python
from cs50 import SQL
# import tools untuk website
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# mengatur nama aplikasi
app = Flask(__name__)

# dipakai untuk koneksi ke database
db = SQL("sqlite:///score.db")


@app.route("/", methods=["GET", "POST"])
# ketika route "/" dipanggil/diakses, maka fungsi index() dieksekusi
def index():
    # jika request yg dilakukan oleh pengguna adalah post, maka eksekusi kode dalam if
    if request.method == "POST":

        # Access form data / membaca data yang diisilkan pada form
        name = request.form.get("name")# ambil data dari input name
        score = request.form.get("score")# ambil data dari imput month

        # insert data into database, masukkan data name, month, day ke database
        db.execute("INSERT INTO score (name, score) VALUES(?, ?)", name, score)
        #index_test=db.execute("SELECT * ")

        # Go back to homepage
        return redirect("/")

    else:

        # ambil seluruh data dari tabel birthdays, simpan di variabel birthdays
        students = db.execute("SELECT * FROM score")    

        # salin isi variabel birthdays ke birthdays, lalu kirim ke index.html
        return render_template("index.html", students=students)
    

