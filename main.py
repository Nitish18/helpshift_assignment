import os 
import argparse
import sys
import traceback

current_dir = os.getcwd()
sys.path.append(current_dir)


def main():
    """
    entry point of python program.

    Returns
    ------
    STDOUT
        prints output on terminal.
    """
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("input_file", help="Taking input from a file")
        if not len(sys.argv) > 1:
            # no argument is passed, taking input from command line (CLI)
            execute_using_cli()
        else:
            # arguments not supported.
            print("more arguments not supported. please try again.")
    except Exception as e:
        traceback.print_exc()



def execute_using_cli():
    """
    method called during CLI.
    User can type commands to perform particular operation.

    Returns
    ------
    STDOUT
        prints output on terminal.
    """
    while(1):
        print("1) Add contact 2) Search 3) Exit")
        user_input = input()
        
        if validate_user_input(user_input):
            if int(user_input) == 3:
                print("Happy Searching")
                break
            else:
                print("processing")
        else:
            print("Input is not valid. Try again !")
        
    

def validate_user_input(user_input = None):
    """
    method to validate user input.
    
    Parameters
    ----------
    user_input : string
        input typed by user
    
    Returns
    ------
    Boolean
        true (user input is valid) or false (invalid input).
    """
    try:
        user_input = int(user_input)
        if user_input >= 1 and user_input <= 3:
            return True
        return False
    except Exception as e:
        return False
    
    
if __name__ == '__main__':
    main()