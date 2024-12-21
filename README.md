# **Problem Reporting Web Application with Data Visualization**  

## **Project Structure**  
```
project-directory/
│
├── templates/                       # HTML templates for rendering web pages  
│   ├── form.html                    # HTML form for submitting problems  
│
├── complaints_app.py                # Main Flask application  
├── create_problems_db.sql           # SQL script to create the database and table  
├── query_problems.sql               # SQL queries for testing and fetching data  
├── requirements.txt                 # Python dependencies  
└── README.md                        # Documentation  
```

---

## **Installation and Setup**  

### **1. Clone the repository**  
```bash
git clone https://github.com/kwoba98/Problem-Reporting-Web-App.git
cd problem-reporting-app
```

### **2. Set up the environment**  
- **Install Python** (version 3.8 or above).  
- Create a virtual environment:  
```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### **3. Install dependencies**  
```bash
pip install -r requirements.txt
```

### **4. Configure the MySQL Database**  
- Log in to MySQL Workbench or command line and create the database:  
```sql
SOURCE create_problems_db.sql;
```

- Verify the table structure using:  
```sql
SOURCE query_problems.sql;
```

- Update **`DB_CONFIG`** in `complaints_app.py` with your database credentials:  
```python
DB_CONFIG = {
    "host": "localhost",
    "user": "your-username",
    "password": "your-password",
    "database": "problem_reportingapp"
}
```

### **5. Run the Flask Application**  
```bash
python complaints_app.py
```

- Open your browser and visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)  

---

## **How the App Works**  

1. **Submit Complaints** - Users submit problems with details such as category, description, and location.  
2. **Store in MySQL** - The app stores submissions securely in the MySQL database.  
3. **View Visualizations** - Complaint categories and counts are dynamically visualized using Chart.js.  

---

## **Endpoints**  

### **1. Submit Problem**  
- **Endpoint**: `/submit_problem`  
- **Method**: POST  
- **Description**: Submit a problem with category, description, and location.  
- **Payload Example**:  
```json
{
    "category": "Water",
    "description": "Leaking pipe near school",
    "location": "5th Avenue"
}
```

- **Response**:  
```json
{
    "message": "Problem submitted successfully"
}
```

---

### **2. Get Complaint Categories**  
- **Endpoint**: `/get-categories`  
- **Method**: GET  
- **Description**: Retrieve all categories and their respective counts.  
- **Response**:  
```json
[
    {"category": "Water", "count": 10},
    {"category": "Electricity", "count": 7}
]
```

---

## **Example Usage**  

### **1. Submit a Problem**  
```bash
curl -X POST http://127.0.0.1:5000/submit_problem \
-H "Content-Type: application/json" \
-d '{
    "category": "Road",
    "description": "Potholes causing traffic issues",
    "location": "Main Street"
}'
```

### **2. Get Category Counts**  
```bash
curl -X GET http://127.0.0.1:5000/get-categories
```

- Example Output:  
```json
[
    {"category": "Road", "count": 5},
    {"category": "Electricity", "count": 3}
]
```

---

## **Database Scripts**  

### **create_problems_db.sql**  
```sql
CREATE DATABASE IF NOT EXISTS problem_reportingapp;

USE problem_reportingapp;

CREATE TABLE IF NOT EXISTS problems (
    category VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    location VARCHAR(255) NOT NULL
);
```

### **query_problems.sql**  
```sql
USE problem_reportingapp;

-- Select all problems
SELECT * FROM problems;

-- Get complaint categories with counts
SELECT category, COUNT(*) AS count FROM problems GROUP BY category;
```

---

## **Technologies Used**  
- **Backend**: Flask (Python)  
- **Frontend**: HTML, JavaScript, Chart.js  
- **Database**: MySQL  
- **API Testing**: cURL/Postman  

---

Now you're ready to test, deploy, and improve the application further!
