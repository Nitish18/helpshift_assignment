import os 
import argparse
import sys
import traceback

from trie_datastructure import Trie

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
    CLI mode.
    User can type commands to perform particular operation.

    Returns
    ------
    STDOUT
        prints output on terminal.
    """

    # initializing trie class object.
    my_trie = Trie()

    while(1):
        print("1) Add contact 2) Search 3) Exit")
        user_input = input()
        
        if validate_user_input(user_input):
            if int(user_input) == 3:
                print("Happy Searching")
                break
            else:
                input_name = input("Enter name: ").split(' ')
                res = execute(user_input, input_name, my_trie)
                if res:
                    # printing on STDOUT the final result.
                    for item in res:
                        print(item)
        else:
            print("Input is not valid. Try again !")


def execute(user_input=None, input_name=[], my_trie = None):
    '''
    function to execute main business logic of code flow according to input type.

    Args:
        user_input(String): type of operation such as 1 (Insert), 2 (Searching)
        input_name(List): list of items entered by user in format of first name and last name.
        my_trie(Object): instance of Trie class.

    Return:
        Set: set of result string incase of valid input.
        List: in case of invalid input

    '''
    is_input_valid = validate_user_input(input_name, True)
    if is_input_valid:
        name = ''
        for item in input_name:
            name += str(item)
            name += str(" ")
        name = name.rstrip()

        if int(user_input) == 1:
            # inserting name into trie.
            my_trie.insert(name)
        elif int(user_input) == 2:
            # searching through trie.
            search_result = []
            if my_trie.search(name):
                search_result.append(name)
            search_result.extend(my_trie.prefix_search(name))
            return set(search_result)
    else:
        return ["Input name is not valid."]
        
    
def validate_user_input(user_input = None, check_name = False):
    """
    function to validate user input.
    checking two things :
    1. if name is valid i.e having maximum two words for first and last name.
    2. if user input is a valid integer.
    
    Parameters
    ----------
    user_input : string
        input typed by user
    check_name : Boolean
        type of input validation.
    
    Returns
    ------
    Boolean
        true (user input is valid) or false (invalid input).
    """
    try:
        if check_name:
            if len(user_input)>2:
                return False
            return True
        else:
            user_input = int(user_input)
            if user_input >= 1 and user_input <= 3:
                return True
            return False
    except Exception as e:
        return False
    
    
if __name__ == '__main__':
    main()