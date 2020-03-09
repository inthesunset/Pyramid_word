# Develop a web service for testing pyramid word

## I use python Flask to implement light web service. Backend implementation is straightforward, so I simply gather code into app.py file. Each time we have a request, we run is_pyramid function to test the input string and return the corresponding bool value. Notice that no database is involved for this service.

## We can set up virtual environment for this application through virtualenv, but I did not do it for simplicity.

## How does it work?
  1. pip install -r requirements.txt
  2. python app.py
  3. Open web browser to http://localhost:5000/
  4. input a string in the box and click test button
  5. The result will show up
  6. Click go back button to test next string

## The requirements.txt file contains non-required packages(since I have other packages installed in my local machine). You can replace the first step with pip install flask.

## snapshot of test cases: 'banana' and 'bandana'
