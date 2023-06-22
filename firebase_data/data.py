from firebase import firebase
import json
firebase = firebase.FirebaseApplication('https://finance-market-new-blog-default-rtdb.firebaseio.com', None)

def get_data(file):
    # result = firebase.get('/', None)
    # resultList = [value for key, value in result.items()]
    # return resultList
    f = open(file)
  
    # returns JSON object as 
    # a dictionary
    data = json.load(f)
    f.close()
    return data['articles']