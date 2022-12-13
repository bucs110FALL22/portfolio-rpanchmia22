import Holidays
import Weather
import string

def main():
  
  year = int(input("Enter the past year of your holiday: "))
  day = int(input("Enter the day of your holiday: "))
  month = int(input("Enter the month of your holiday as a number: "))
  
  holiday = Holidays.getHolidays(day,month,year)
  holidayResult = holiday.get()
  holiname = holidayResult['response']['holidays'][0]['name']
  print("Holiday: " + str(holiname))
  
  if day < 10:
    day = "0" + str(day)
  if month < 10:
    month = "0" + str(month)
  date = str(year)+"-"+str(month)+"-"+str(day)
  print("Date: " + str(date))
  
  state = str(input("Enter the full name of a state: "))
  state = string.capwords(state)
  print("State: " + str(state))
  
  weather = Weather.getWeather(state,date)
  weatherResult = weather.get()
  temp = weatherResult['historical'][date]['avgtemp']
  print("Temperature: " + str(temp))
  
  print("In " + str(state) + ", on " + str(holiname) + " " + str(year) + " the average temperature was " + str(temp) + " degrees Fahrenheit.")
  
main()