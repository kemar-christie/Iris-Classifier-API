# 🌸 Iris-Classifier-API

<br>

## 📝 Description
A simple and fast REST API built with FastAPI that predicts the species of an Iris flower using a trained machine learning model. This project uses the classic Iris dataset and demonstrates how to serve a scikit-learn model through a production-ready API. The Iris dataset consists of 150 samples of iris flowers from three different species: Setosa, Versicolor, and Virginica. Each sample includes four features: sepal length, sepal width, petal length, and petal width. 

<br>

## 🔧 Key Features
* 🔮 Predict Iris species using sepal and petal measurements
* ⚡ Built with FastAPI for speed and automatic documentation
* 🧠 Powered by scikit-learn
* 🧹 Utilizes pandas for efficient data preprocessing and manipulation
* 🚀 Runs on Uvicorn, an ASGI server optimized for high performance
* 📄 Swagger UI available at /docs (http://127.0.0.1:8000/docs)

<br>

## 🖥️ Technologies Used
* 🐍 Python
* 🏫 Scikit-learn
* 🐼 Pandas
* ⚡ FastAPI
* 🚀 Uvicorn

<br>

## 📊 Model Details
* **Dataset**: Iris Dataset
* **Algorithm**: Logistic Regression
* **Classes**:
  - 0: Iris-setosa
  - 1: Iris-versicolor
  - 2: Iris-virginica

  Petal Length:
  - Iris setosa: 1.0 to 1.9 cm 
  - Iris versicolor: 3.0 to 5.1 cm
  - Iris virginica: 4.5 to 6.9 cm
    
  Petal Width:
  - Iris setosa: 0.1 to 0.6 cm
  - Iris versicolor: 1.0 to 1.8 cm
  - Iris virginica: 1.4 to 2.5 cm

<br>

## ▶️ How to Run IRIS-CLASSIFIER-API
1. Clone the Repository
   ```bash
   git clone https://github.com/kemar-christie/Iris-Classifier-API
   cd Iris-Classifier-API
   ```

2. Install Dependencies
<br> Ensure you have Python 3.9+ installed. Then, install the required libraries by navigating to the folder where "requirements.txt" is located:
   ```bash
   pip install -r requirements.txt
   ```

3. Run Generator Script
   ```bash
   cd code
   python local_ml_model_generator.py
   ```

4. Start the API
    ```bash
    uvicorn interface_API:app --reload
    ```
    Visit http://127.0.0.1:8000/docs to access the interactive Swagger UI.

5. Test the API by Sending a Prediction Request 
<br> Endpoint: POST /predict
<br> Request JSON:
    ```json
    [6.1, 3.1, 5.0, 1.6]
    ```
    ```format
    [sepal_length, sepal_width, petal_length, petal_width]
    ```

    Response:
    ```json
    {
      "prediction": 2
    }
    ```

<br>

## 🛠️ Project Structure
```text
Iris-Classifier-API/
  ├── .gitignore                                             
  ├── LICENSE                                               
  ├── NOTICE                                                 
  ├── README.md                                              
    Iris-Classifier-API/code
      ├── interface_API.py                                    
      ├── local_ml_model_generator.py                          
      ├── local_ml_model.pkl                                   
    Iris-Classifier-API/workspace_requirements
      ├── requirements.txt                                   
```
