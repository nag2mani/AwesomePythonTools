"""
This module will convert Celsius to fahrenheit and tell if weather is cold,nice or hot.
Author: Nagmani kumar
Date: 10 Dec 2022
"""
def cel_to_fahrenheit(c):
    """
    Converts the input Temperature(in celsius) to Fahrenheit.
    
    It will print weather is cold when 
    when temp is less than 60, weather is nice betweeen 60 and 85 (including both)
    and weather is hot when more than 85.

    Parameter c: temperature in celcius for converting into fahrenheit.
    Precondition: Input must be either int or float.
    
    >>> cel_to_fahrenheit(100)
    Weather is hot
    >>> cel_to_fahrenheit(60)
    Weather is hot
    >>> cel_to_fahrenheit(25)
    Weather is Nice
    >>> cel_to_fahrenheit(0)
    Weather is cold
    >>> cel_to_fahrenheit(12.6)
    Weather is cold

    """
    #if function is vary big then you can use comment to undarstand.
    faren=(c * 1.8) + 32
    print("Weather is cold" if faren<60 else ("Weather is Nice" if faren<=85 else "Weather is hot"))

c=float(input("entre your temp in celcius: "))
if __name__=='__main__':
    import doctest
    doctest.testmod()

cel_to_fahrenheit(c)

