from knapsack import Driver

def main():
    # Test case using max weight of 7 and values given in assignment
    max_weight = 7  # Max weight the knapsack can carry
    weights = [5, 1, 3, 3, 5, 2, 3, 5, 7, 2, 7, 2, 2, 3, 3]  # Weights of the items
    values = [5, 8, 6, 3, 6, 10, 3, 5, 8, 2, 5, 4, 8, 9, 7]  # Values of the items

    # Create the driver class and solve the problem
    driver = Driver(max_weight, weights, values)
    driver.solve()

if __name__ == '__main__':
    main()