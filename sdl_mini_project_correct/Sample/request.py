import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Crop_Year':2025, 'Crop':19, 'Area':600})

print(r.json())