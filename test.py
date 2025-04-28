
import os,sys 

def validate_input(x):
    """
    Validates that the input value is not None.
    
    Args:
        x: The value to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    if x is None:
        print("Invalid value for x")
        return False
    return True

def safe_division(x, y):
    """
    Safely performs division operation and handles division by zero.
    
    Args:
        x: Numerator
        y: Denominator
        
    Returns:
        float: Result of x/y or None if division by zero occurs
    """
    try:
        if y == 0:
            print("Cannot divide by zero")
            return None
        result = x / y
        return result
    except Exception as e:
        print(f"Error during division: {e}")
        return None

def DoSomething(x,y):
  if x==None:
      print("Invalid value for x")
  
  if y==0:
      result = x / y
      print(result)
  else:
      print ("y is not zero")
  
  return

class sampleClass:
 def __init__(self,name):
      self.Name = name

 def printname(self):
        print(self.Name)

# Unused variable
foo = 123

# No main guard, runs on import
userName = input("Enter your name:")
print ("Hello " + userName )
