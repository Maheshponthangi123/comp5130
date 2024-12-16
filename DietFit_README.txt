
# **DietFit - FastAPI Server**

## **Overview**
DietFit is a FastAPI-based application that allows users to securely sign up, log in, and manage their dietary and exercise plans. It also provides BMI calculation, daily calorie tracking, and a 7-day meal and exercise plan.

This README will guide you through the steps to set up and run the project locally.

---

## **Prerequisites**
Ensure you have the following installed on your system:
- **Python** (version 3.8 or above)
- **MongoDB** (running locally or on a remote server)
- **Edamam API credentials** (app ID and app key)
- **Virtual Environment** (optional but recommended)

---

## **Installation**

### **1. Clone the Repository**
Run the following command in your terminal to clone the project repository:
```bash
git clone https://github.com/your-repo/DietFit-main.git
cd DietFit-main
```

### **2. Create and Activate a Virtual Environment**
It is recommended to use a virtual environment for isolating dependencies.

- **For Windows**:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

- **For Linux/Mac**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

### **3. Install Required Dependencies**
Run the following command to install all dependencies:
```bash
pip install -r requirements.txt
```

---

## **Configuration**

### **MongoDB Setup**
1. Make sure MongoDB is running on your local machine or a remote server.
2. Update the MongoDB connection string in `key_data.py`:
   ```python
   MONGO_URI = "your-mongo-connection-string"
   DB_NAME = "dietfit"
   ```

### **Edamam API Configuration**
1. Obtain Edamam API credentials (app ID and app key).
2. Add the credentials to `key_data.py`:
   ```python
   post_app_id = "your-edamam-app-id"
   post_app_key = "your-edamam-app-key"
   ```

---

## **Running the Application**

### **1. Activate the Virtual Environment**
If the virtual environment is not already activated:
- For Windows:
   ```bash
   .\venv\Scripts\activate
   ```
- For Linux/Mac:
   ```bash
   source venv/bin/activate
   ```

### **2. Run the Application**
Start the FastAPI server by running:
```bash
python app.py
```

### **3. Access the Application**
Once the server is running, you can access it at:
```
https://0.0.0.0:7000
```

- API Documentation (Swagger UI):
   ```
   http://127.0.0.1:7000/docs
   ```

- Example Logs:
   ```
   INFO: Started server process [12345]
   INFO: Uvicorn running on https://0.0.0.0:7000
   ```

---

## **Available Endpoints**

### **User Management**
| Endpoint        | Method | Description            |
|-----------------|--------|------------------------|
| `/signupCheck`  | POST   | User signup            |
| `/loginCheck`   | POST   | User login             |
| `/getFirstname` | POST   | Get user’s first name  |

### **Health Calculations**
| Endpoint             | Method | Description                 |
|----------------------|--------|-----------------------------|
| `/calculate_bmi`     | POST   | Calculate BMI               |
| `/calculate_calories`| POST   | Calculate daily calorie intake |

### **Diet and Exercise Plans**
| Endpoint        | Method | Description            |
|-----------------|--------|------------------------|
| `/viewDiet`     | POST   | Generate 7-day diet plan|
| `/getExercises` | POST   | Generate 7-day exercises|

---

## **Stopping the Server**
To stop the server, press `CTRL + C` in the terminal where the application is running.

---

## **Troubleshooting**
| Problem                           | Solution                                   |
|----------------------------------|-------------------------------------------|
| **MongoDB Connection Error**      | Verify MongoDB URI and server status.     |
| **Port Already in Use**           | Stop any other process using port 7000.   |
| **SSL Certificate Error**         | Verify `cert.pem` and `key.pem` files.    |
| **API Key Issues**                | Ensure valid Edamam API keys in `key_data.py`. |

---

## **Notes**
- The application requires Edamam API access for diet plan generation.
- Ensure MongoDB is running before starting the server.

---

## **License**
This project is licensed under the MIT License.
