

class TemperatureCounter:
    @staticmethod
    def celsius_to_fahrenheit(c):
#Convert Celsius to Fahrenheit.Convert Celsius to Fahrenheit.
     return (c * 9/5) + 32
 
 # for EExample
celsius_temp = 25
fahrenheit_temp = TemperatureCounter.celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp}°C is equal to {fahrenheit_temp}°F")
