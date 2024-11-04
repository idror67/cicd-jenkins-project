from flask import Flask, redirect, render_template, request
import os
from dotenv import load_dotenv

load_dotenv()

# Retrieve the DATABASE_TYPE environment variable, defaulting to 'MYSQL' if not set
db_to_use = os.getenv("DATABASE_TYPE", "MYSQL")

if db_to_use == "MYSQL":
    from data_sql import (get_contacts, findByNumber,
                          check_contact_exist, search_contacts,
                          create_contact,
                          delete_contact, update_contact_in_db)
elif db_to_use == "MONGO":
    from data_mongo import (get_contacts, findByNumber,
                            check_contact_exist, search_contacts,
                            create_contact,
                            delete_contact, update_contact_in_db)

app = Flask(__name__)

@app.route('/')
def hello():
    return redirect('/viewContacts')

@app.route('/saveUpdatedContact/<number>', methods=['POST'])
def saveUpdatedContact(number):
    name = request.form['fullname']
    phone = request.form['phone']
    email = request.form['email']
    gender = request.form['gender']
    update_contact_in_db(number, name, phone, email, gender)
    return redirect('/viewContacts')

@app.route('/search', methods=['POST'])
def search():
    search_name = request.form['search_name']
    search_results = search_contacts(search_name)
    return render_template('index.html', contacts=search_results)

if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=5052)