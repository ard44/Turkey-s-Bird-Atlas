from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('bird_atlas.db')
    conn.row_factory = sqlite3.Row
    return conn


def clear_db():
    conn = get_db_connection()
    conn.execute('DELETE FROM observations')
    conn.commit()
    conn.close()


clear_db() 

@app.route('/')
def index():
    conn = get_db_connection()
    birds = conn.execute('SELECT * FROM species').fetchall()
    
    
    obs = conn.execute('''
        SELECT observations.*, species.name_tr 
        FROM observations 
        JOIN species ON observations.bird_id = species.id
    ''').fetchall()
    
    conn.close()
    return render_template('index.html', birds=birds, observations=obs)

@app.route('/add_observation', methods=['POST'])
def add_observation():
    bird_id = request.form['bird_id']
    note = request.form['note']
    conn = get_db_connection()
    conn.execute('INSERT INTO observations (bird_id, note) VALUES (?, ?)', (bird_id, note))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM observations WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)