# 🧠 Employee Salary Prediction

This project was developed as part of my **Virtual Internship Program** by Edunet Foundation in collaboration with AICTE and industry partners. The objective is to build a machine learning model that predicts employee salary  based on job attributes like title, experience, company size, location, and more.

---

## 📌 Project Objective

To predict the salary category of an employee (e.g., Low, Mid, High) using machine learning algorithms based on job-related features.

---

## 🧰 Tech Stack Used

| Tool/Library         | Purpose                            |
|----------------------|-------------------------------------|
| Python               | Core Programming Language           |
| Pandas, NumPy        | Data Handling and Processing        |
| Matplotlib, Seaborn  | Data Visualization                  |
| scikit-learn         | ML Models, Preprocessing            |
| GradientBoosting     | Selected ML Model for Prediction    |
| Flask                | Backend Web Application Framework   |
| HTML, CSS, JS        | Frontend for User Interaction       |

---

## 🗃️ Dataset Information

- Rows: ~15,000
- Columns: 19
- Key Columns Used:
  - `job_title`
  - `experience_level`
  - `employment_type`
  - `company_location` 
  - `company_size`
  - `remote_ratio`

Preprocessing included:
- Dropping irrelevant columns (`job_id`, `salary_currency`, etc.)
- Label encoding categorical variables
- Mapping locations to regions (Asia, Europe, etc.)
- Grouping job titles into major roles (Engineer, Analyst, etc.)
- Converting continuous salary to categorical labels (Low, Mid, High or 8 classes)

---

## 📈 Model Performance

- **Algorithm Used**: Gradient Boosting Classifier
- **Accuracy**: ~84% (on test data with 3 salary categories)
- **Feature Importance** analyzed and tuned
- Dataset split into Train/Test (80/20)

---

## 💻 Web Interface

The project is integrated with a **Flask web app** where users can input job details and get salary category predictions in real-time.

### Screenshots
1. Model Prediction Interface  
2. Code Execution Output  
3. Dataset Preview  
4. Feature Importance Graph  
5. Flask Form UI  

> *(Add actual screenshots in a folder or embed in the README if hosted)*

---

## 🚀 How to Run

1. Clone the repository  
   ```bash
   git clone https://github.com/your-username/employee-salary-predictor
   cd employee-salary-predictor
