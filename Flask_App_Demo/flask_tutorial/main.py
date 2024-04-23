from flask import Flask, redirect, url_for, request, Response, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'testing'
app.config['MYSQL_PASSWORD'] = 'RM@!2992Dm'
app.config['MYSQL_DB'] = 'website'

mysql = MySQL(app)

@app.route('/', methods = ["POST", "GET"])
def main_page():
    return render_template("index.html")

@app.route('/a_1', methods = ["POST", "GET"])
def a_1():
    if request.method == "POST":
        print("HI")
        print(request.method)
        print(request.form["box"])  

        print("TEST")

        cursor = mysql.connection.cursor()
        cursor.execute("select * from mytable where BondNumber like %s", (request.form["box"],))

        data = cursor.fetchone()

        cursor.close()

    return render_template("index.html", a_1_data = data) 


@app.route('/a_2', methods = ["POST", "GET"])
def a_2():
    if request.method == "POST":
        cursor = mysql.connection.cursor()
        selected_party = request.form['party-select']
        cursor.execute(f"SELECT * FROM mytable WHERE `{selected_party}` like %s", (request.form["box"],))


        




        data = cursor.fetchall()

        cursor.close()
        
    return render_template("index.html", a_2_data = data) 


@app.route('/a_3', methods = ["POST", "GET"])
def a_3():
    data = []  # Initialize data outside of the if block
    if request.method == "POST":
       cursor = mysql.connection.cursor()
       party_name = request.form["party-select"]
       print("Party Name:", party_name) 
       cursor.execute("SELECT COALESCE(YEAR(NewColumnName), 'Unknown') AS Year, SUM(Denominations) AS TotalDenominations FROM party WHERE partyname LIKE %s GROUP BY Year, partyname", (party_name,))
       query = "SELECT COALESCE(YEAR(NewColumnName), 'Unknown') AS Year, SUM(Denominations) AS TotalDenominations FROM party WHERE partyname LIKE %s GROUP BY Year, partyname"
       data = cursor.fetchall()
       print("Query:", query)  # Debugging output

       cursor.close()
    
    if len(data) == 0:
        return render_template("index.html", a_3_data=[["Not Found !!!"]]) 

    return render_template("index.html", a_3_data=data)



@app.route('/a_4', methods = ["POST", "GET"])
def a_4():
    if request.method == "POST":
        cursor = mysql.connection.cursor()
        
        party_name = str(request.form["search-input"])
        cursor.execute("SELECT `Date ofPurchase`,SUM(Denominations) FROM mytable2 WHERE `Name of the Purchaser` LIKE %s GROUP BY `Date ofPurchase`", (party_name,))
         
        

        data = cursor.fetchall()
        data_list = [[str(row[0]), float(row[1])] for row in data]

        cursor.close()
    
    if len(data) == 0:
        return render_template("index.html", a_4_data = [["Not Found !!!"]]) 

    return render_template("index.html", a_4_data = data,data=data_list)
@app.route('/a_5', methods = ["POST", "GET"])
def a_5():
    if request.method == "POST":
        cursor = mysql.connection.cursor()
        
        party_name = str(request.form["search-input"])
        cursor.execute("SELECT DISTINCT `Name of the Purchaser` FROM mytable2 WHERE `BondNumber` IN (SELECT `BondNumber` FROM mytable WHERE `Name of the Political Party` = %s)", (party_name,))
         
        

        data = cursor.fetchall()
        # data_list = [[str(row[0]), float(row[1])] for row in data]

        cursor.close()
    
    if len(data) == 0:
        return render_template("index.html", a_5_data = [["Not Found !!!"]]) 

    return render_template("index.html", a_5_data = data,)
def a_6():
    if request.method == "POST":
        cursor = mysql.connection.cursor()
        
        party_name = str(request.form["search-input"])
        cursor.execute("SELECT DISTINCT `Name of the Purchaser` FROM mytable WHERE `BondNumber` IN (SELECT `BondNumber` FROM mytable2 WHERE `Name of Purchaser` = %s)", (party_name,))
         
        

        data = cursor.fetchall()
        # data_list = [[str(row[0]), float(row[1])] for row in data]

        cursor.close()
    
    if len(data) == 0:
        return render_template("index.html", a_5_data = [["Not Found !!!"]]) 

    return render_template("index.html", a_6_data = data,)
if __name__ == '__main__':
   app.run(host="0.0.0.0", port="80", debug = True) 
