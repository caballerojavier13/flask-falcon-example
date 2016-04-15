# Flask and Falcon Example

Example of an API in using Flask and Falcon that implement the following:

    GET /
    Response: POST a JSON body to get its keys
    
  
    POST /
    Request-Body: { "foo": "bar", "fizz": "buzz" }
    Response: { 
      "foo": "bar", 
      "fizz": "buzz",
      "keys" : ["foo", "fizz"]
    }
    

## Running the Demo

Be sure to run this in a [Virtual Environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/) with Python 3.5
    
    pip install -r requirements.txt 
    
    For Falcon demo:
        
        gunicorn falcon-demo:api
        
    For Flask demo:
    
        python flask-demo.py
        
    
