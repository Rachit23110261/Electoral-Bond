from flask import Flask, redirect, url_for, request, Response, render_template
from sqlalchemy import text
from sqlalchemy import create_engine, text
import sqlalchemy
import pymysql
from flask_mysqldb import MySql

app = Flask(__name__)

@app.route('/')
def main_page():
    engine = create_engine("mysql+pymysql://test:password@10.7.35.113:3306/imdb")

    with engine.connect() as conn:
        sql = text('select * from genre')
        data = conn.execute(sql)

    print(data)
    return render_template("index.html")


if __name__ == '__main__':
   app.run(host="0.0.0.0", port="80", debug = True) 