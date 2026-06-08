from flask import Flask, render_template, request, redirect

app = Flask(__name__)


observations = []
obs_id_counter = 1


import sqlite3
def get_db_connection():
    conn = sqlite3.connect('bird_atlas.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    birds = conn.execute('SELECT * FROM species').fetchall()
    conn.close()
    return render_template('index.html', birds=birds, observations=observations)

@app.route('/add_observation', methods=['POST'])
def add_observation():
    global obs_id_counter
    bird_id = request.form['bird_id']
    note = request.form['note']
    
    
    conn = get_db_connection()
    bird = conn.execute('SELECT name_tr FROM species WHERE id = ?', (bird_id,)).fetchone()
    conn.close()
    
    observations.append({
        'id': obs_id_counter,
        'name_tr': bird['name_tr'],
        'note': note
    })
    obs_id_counter += 1
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    global observations
    observations = [ob for ob in observations if ob['id'] != id]
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)