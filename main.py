from knapsack import Driver
import csv 


def input_from_csv(file_name):
    """
    Simple function that reads the item weights and values from a CSV file.
    Example of csv file needed is knapsack.csv
    
    Args:
    file_name (str): The path to the CSV file containing item weights and values.
    
    Returns:
    tuple: A tuple containing two lists: 
           - weights: List of item weights
           - values: List of item values
    """
    weights = []  # List to store weights of items
    values = []   # List to store values of items
    
    # Open the CSV file for reading
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)  # Create a CSV reader object
        for row in reader:
            if row:  # Ignore empty rows
                # Append the weight and value for each item (assuming CSV format: weight, value)
                weights.append(int(row[0]))  # The first column is the weight
                values.append(int(row[1]))   # The second column is the value
    # Return the lists of weights and values
    return weights, values


def main():
    print("Welcome to the Knapsack Problem Solver!")
    run = True

    while run: 
        print("\n")
        input_method = input("Enter 'manual' to input values manually, 'csv' to import from a CSV file, or 'exit' to exit: ").strip().lower()

        if input_method == 'manual':
            max_weight = int(input("Enter the maximum weight of the knapsack: "))
            num_items = int(input("Enter the number of items: "))
            weights = [int(input(f"Enter weight for item {i+1}: ")) for i in range(num_items)]
            values = [int(input(f"Enter value for item {i+1}: ")) for i in range(num_items)]
            # Create the driver class and solve the problem
            driver = Driver(max_weight, weights, values)
            driver.solve()
        elif input_method == 'csv':
            file_name = input("Enter the CSV file name (with path): ")
            weights, values = input_from_csv(file_name)
            max_weight = int(input("Enter the maximum weight of the knapsack: "))
            # Create the driver class and solve the problem
            driver = Driver(max_weight, weights, values)
            driver.solve()
        elif input_method == 'exit':
            print('Goodbye')
            run = False
        else:
            print("Invalid option. Please restart the program and choose 'manual', 'csv', or 'exit'.")
            return


if __name__ == "__main__":
    main()
