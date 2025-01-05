import requests

test_data = {
    "CD_Account": 1, # whether he/she has financial stability or not (certicate of deposit)
    "Education": 1, # education level in my case (1-basic, 2-intermediate, 3-master)
    "CCAvg": 4.6, # average spending on credit cards -- in thousands
    "Mortgage": 1, # mortgage loan amount 
    "Age": 25, # age of the application
    "Income": 100 # income 
}

response = requests.post("http://localhost:8000/predict", json=test_data)
print(response.json())
