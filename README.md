knapsack.py:

  Knapsack Class:
    Initializes the values for max weight, list of item weights, list of item values, and the number of items.
    Solves the 0/1 Knapsack problem and backtracks to display the solution in the terminal.
    
  Driver Class:
    Initializes the Knapsack class and is used by both test.py and main.py to solve the problem.

  
test.py:

  Defines the parameters of the Knapsack problem with predefined values (max weight = 7).
  This file will run the knapsack solver with those predefined values and display the resulting table.

  
main.py:

  Provides a user interface to allow the user to either:
    Manually input the weights, values, and max weight.
    Import a CSV file containing the item weights and values.
  The user is prompted to choose one of the following options:
    manual: Manually input the knapsack parameters.
    csv: Upload a CSV file with the item weights and values.
    exit: Exit the program.


User Input Details:

  Manual Input:
    The user will first be prompted for the max weight of the knapsack and the number of items.
    Then, the user must input the list of item weights, followed by the corresponding list of item values.
  
  CSV Input:
    The user will provide the file path to the CSV containing the weights and values.
    The user will also input the max weight of the knapsack.
    CSV Format:
    The CSV must have no header.
    The first column ([0]) contains the item weights.
    The second column ([1]) contains the item values.
    An example of this is provide in knapsack.csv in the repository.


Program Flow:

  When running main.py, the program prompts the user for input.
  If the user chooses manual input, they provide the max weight, number of items, and the weights/values of the items.
  If the user chooses CSV input, they provide the file path to the CSV and the max weight.
  The program then solves the Knapsack problem using the provided input and displays the solution.
  
Error Handling:

  If an invalid option is entered (neither 'manual' nor 'csv' nor 'exit'), the program will show an error message and prompt the user to choose again.


Let me know if you have any problems!
