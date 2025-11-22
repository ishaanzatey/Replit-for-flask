from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bangalore, India',
        'salary': 'Rs. 10,00,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'New York, USA',
        'salary': '$120,000'
    },
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'San Francisco, USA',
        'salary': '$140,000'
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'Berlin, Germany',
        # 'salary': '€80,000'
    }
]


@app.route('/')
def hello_world():
    return render_template('home.html', jobs=JOBS,
                           company_name="Jovian")




@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)



print(__name__)
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)