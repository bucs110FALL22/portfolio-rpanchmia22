import requests

class getWeather:
  def __init__(self,state=None,date=None):

    '''
    initializes the classes' attributes
    args: (str) state, (str) date
    return: none
    '''
    
    self.url = f"http://api.weatherstack.com/historical?access_key=243af9c780e085a91650e17fb1b9271d&query={state}&historical_date={date}&units=f"

  def __str__(self):
    
    '''
    allows for easy access to url
    args: none
    return: (str) url of website data is grabbed from
    '''
    
    return self.api_url

  def get(self):
    
    '''
    grabs data from url
    args: none
    return: data from web api
    '''
    
    r = requests.get(self.url)
    response = r.json()
    return response



    