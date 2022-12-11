import Holidays
import Weather
import string

def main():
  
  day = int(input("Enter the day of your holiday: "))
  month = int(input("Enter the month of your holiday as a number: "))
  year = int(input("Enter a past year: "))
  
  holiday = Holidays.getHolidays(day,month,year)
  holidayResult = holiday.get()
  holiname = holidayResult['response']['holidays'][0]['name']
  print("Holiday: " + str(holiname))
  
  if day < 10:
    day = "0" + str(day)
  if month < 10:
    month = "0" + str(month)
  date = str(year)+"-"+str(day)+"-"+str(month)
  print("Date: " + str(date))
  
  state = str(input("Enter the full name of a state: "))
  state = string.capwords(state)
  print("State: " + str(state))
  
  weather = Weather.getWeather(state,date)
  weatherResult = weather.get()
  temp = weatherResult['historical'][date]['avgtemp']
  print("Temperature: " + str(temp))
  
  print("In " + str(state) + ", on " + str(holiname) + " in " + str(state) + " the average temperature was " + str(temp) + " degrees Fahrenheit.")
  
main()