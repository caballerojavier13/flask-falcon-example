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
    
