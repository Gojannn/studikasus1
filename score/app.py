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
        db.execute("INSERT INTO score(name, score)VALUES(?, ?)", name, score)
        #index_test=db.execute("SELECT * ")

        # Go back to homepage
        return redirect("/")

    else:

        # ambil seluruh data dari tabel birthdays, simpan di variabel birthdays
        students = db.execute("SELECT * FROM score")    

        # salin isi variabel birthdays ke birthdays, lalu kirim ke index.html
        return render_template("index.html", students=students)
    
@app.route("/edit/<id>", methods=["GET", "POST"])
def edit_data(id):
    if request.method == "GET":
        ubah = db.execute("SELECT * from score WHERE id = ?", id)[0]
        print(ubah)
        return render_template("edit.html",ubah=ubah)
    elif request.method == "POST":
        ubah_name = request.form.get("name")
        ubah_score = request.form.get("score")
        db.execute('UPDATE score set name = ?, score = ? where id = ?', ubah_name, ubah_score, id)
        return redirect("/")
    
@app.route("/delete/<id>", methods=["GET"])
def delete(id):
    db.execute("delete from score where id = ?", id)
    return redirect("/")