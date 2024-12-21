from flask import Flask, request, jsonify, render_template
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin support

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'fredrickson'
app.config['MYSQL_DB'] = 'problem_reportingapp'

# Initialize MySQL
mysql = MySQL(app)

# Route to serve the HTML form
@app.route('/')
def home():
    # Fetch categories for visualization
    categories = get_categories_data()  # This will return a list of categories and their counts
    return render_template('form.html', categories=categories)

# Function to get the categories data from MySQL for visualization
def get_categories_data():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT category, COUNT(*) FROM problems GROUP BY category")
    data = cursor.fetchall()
    cursor.close()
    
    # Format data for visualization
    categories = [{"category": row[0], "count": row[1]} for row in data]
    return categories

# Endpoint to submit a problem
@app.route('/submit_problem', methods=['POST'])
def submit_problem():
    if request.content_type == 'application/json':
        # Handle JSON request payload
        data = request.json
        category = data.get('category')
        description = data.get('description')
        location = data.get('location')
    else:
        # Handle form-encoded data
        category = request.form.get('category')
        description = request.form.get('description')
        location = request.form.get('location')
        # Handle "Other" category if specified
        if category == 'other':
            category = request.form.get('other-category')

    # Validate inputs
    if not category or not description or not location:
        return jsonify({"error": "All fields are required"}), 400

    try:
        # Insert the problem into the database
        cursor = mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO problems (category, description, location) VALUES (%s, %s, %s)",
            (category, description, location)
        )
        mysql.connection.commit()
        cursor.close()

        return jsonify({"message": "Problem submitted successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to get categories data (for AJAX or other requests)
@app.route("/get-categories", methods=["GET"])
def get_categories():
    try:
        categories = get_categories_data()  # Fetch the category counts
        return jsonify(categories), 200
    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
 