from flask import Flask,render_template
from flask_mysqldb import MySQL

app=Flask(__name__)

app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="ram"
app.config["MYSQL_PASSWORD"]="jacob"
app.config["MYSQL_DB"]="jain"
mysql=MySQL(app)

@app.route('/db')
def db():
    cur = mysql.connection.cursor()
    sql="SELECT * FROM soup WHERE id='2'"
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    return render_template('db.html', soup =data)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/jainsoup')
def jainsoup():
    return render_template('jainsoup.html')

if __name__=="__main__":
    app.run(debug=True)
