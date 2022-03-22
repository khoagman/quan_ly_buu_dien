from app import app, pool 
from flask import render_template
from app.forms import TestForm

@app.route('/')
@app.route('/home')
def index():
    return render_template('base.html')

@app.route('/get')
def get():
    connection = pool.acquire()
    cursor = connection.cursor();
    cursor.execute("select id from persons")
    r = cursor.fetchall()
    pool.release(connection)
    return str(r)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form2 = TestForm()
    if form2.validate_on_submit():
        num = form2.num.data
        connection = pool.acquire()
        cursor = connection.cursor();
        query = f"insert into KHOA.persons (id) values ({num})"
        cursor.execute(query)
        connection.commit();
        pool.release(connection)
    return render_template('login.html', form=form2)
