
def get_number(prompt): 
    user_input = input(prompt)
    try:
        value = float(user_input)
        return value
    except ValueError:
        raise ValueError(f"Invalid input '{user_input}'. Please enter a number.")

def calculator():
    while True:
        print("\n -----")
        print("Simple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3.  Multiply")
        print("4.  Divide")
        print("5.  Exit")
        
        choice = input("Choose an operation (1 - 5): ")
        
        if choice == '5':
            print("Exiting the calculator.")
            break
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please select a valid operation.")
            continue
        
        try:
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")
            
            if choice == '1':
                result = num1 + num2 
                op = '+'
                
            elif choice == '2':
                result = num1 - num2
                op = '-'
            
            elif choice == '3':
                result = num1 * num2
                op = '*'
                
            elif choice == '4':
                if num2 == 0:
                    raise ZeroDivisionError("Division by zero is not allowed.")
                result = num1 / num2
                op = '/'
                
        except ValueError as x:
            print(f"operation failed: {x}")
            continue
        except ZeroDivisionError as y:
            print(f"operation failed: {y}")
            continue
        except Exception as e:
            print(f"An unexpected error: {e}")
            continue
        else:
            print(f"The result of {num1} {op} {num2} is: {result}")
            success = True 
        finally: 
            if not success: 
                print("the operation was unsuccessful")
            again = print("Do you want to perform another operation or exit?: ")
            break
                
calculator()
            
            
              
                     
                     
      
        
        
              
        
        
        
  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

#except ValueError as ve:
 #   print("Error:", ve)
#except ZeroDivisionError:
 #   print("Error: Division by zero is not allowed.")
#else:
 #   print(f"The result of {num1} {op} {num2} = {result}")
#finally: 
 #   print("Do you want to perform another operation or exit? ")
    
    
