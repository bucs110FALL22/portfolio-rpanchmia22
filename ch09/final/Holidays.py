import requests

class getHolidays():
  def __init__(self,day=0,month=0,year=0):
    
    '''
    initializes the classes' attributes
    args: (int) day, (int) month, (int) year
    return: none
    '''
    
    self.url = f"https://calendarific.com/api/v2/holidays?api_key=d2a6ae279e873a3baae544cd88d4671437bf9552&country=US&year={year}&day={day}&month={month}"
  
  def __str__(self):
    
    '''
    allows for easy access to url
    args: none
    return: (str) url of website data is grabbed from
    '''
    
    return self.url
  
  def get(self):
    
    '''
    grabs data from url
    args: none
    return: data from web api
    '''
    
    r = requests.get(self.url)
    response = r.json()
    return response
