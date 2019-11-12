# Add a line to import the requests library 
import requests

def url_verify(url):

   good_urls = ['.com', '.net', '.gov', '.edu']
   if not isinstance(url, str):
      return None 
   
   # URL verification function
   if not url[-4:] in good_urls:
      return None
   
   return url
   
def basic_request(url):
   url = url_verify(url)
   if url == None:
      return None
   req = requests.get(url)

   sc = req.status_code
   return sc 

def request_user_agent(url, user_agent):
   url = url_verify(url)
   if url == None:
      return None
   
   if not isinstance(user_agent, str):
      return None 
   
   payload = {'user-agent': user_agent}

   req = requests.get('https://computingconcepts.herokuapp.com/', headers=payload)
   return req.text 


def request_post(url, data):
   url = url_verify(url)
   if url == None:
      return None 
   if data == None or not isinstance(data, dict):
      return None

   req = requests.post('https://computingconcepts.herokuapp.com/post', data=data)
   return req.text
