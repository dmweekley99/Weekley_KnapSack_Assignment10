class Knapsack:
    def __init__(self, max_weight, weights, values):
        '''
        Initialization of Knapsack class taking parameters of max_weight, list of weights, and list of values
        '''
        self.max_weight = max_weight
        self.weights = weights # list of weights
        self.values = values # list of values
        self.num_items = len(weights) # number of items in list
        # Initialize the table with the dimensions of num_items x max_weight
        self.table = [[0] * (max_weight + 1) for _ in range(self.num_items + 1)]
    
    def solve(self):
        '''
        Fills the table with max possible value per given weight with the 
        initialization to be used later in the display_solution function
        '''
        for i in range(1, self.num_items + 1): # iterates through range number of items + 1 to get x dimension
            for w in range(1, self.max_weight + 1): # iterates through range of max weight + 1 to get y dimension
                if self.weights[i - 1] <= w: 
                    # if weight of i - 1 is <= the current max weight choose between:
                    # 1. Not including the current item (value remains the same as without this item)
                    # 2. Including the current item (value + remaining max weight after including the item)
                    self.table[i][w] = max(self.table[i - 1][w], 
                                           self.table[i - 1][w - self.weights[i - 1]] + self.values[i - 1])
                else:
                    # If the item cannot be included (too heavy for current max weight), keep the previous value
                    self.table[i][w] = self.table[i - 1][w]
    
    def display_solution(self):
        w = self.max_weight
        items = []
        total_value = self.table[self.num_items][w]
        total_weight = 0  # Initialize total weight
        
        # Backtrack to find the selected items
        for i in range(self.num_items, 0, -1): # iterates through number of items in reverse
            if total_value != self.table[i - 1][w]: # if the value is not equal to value store in i - 1 x current max weight
                items.append(i - 1)  # Item selected, append its index
                w -= self.weights[i - 1]  # Decrease remaining max weight
                total_value -= self.values[i - 1]  # Decrease the remaining total value
                total_weight += self.weights[i - 1]  # Add the weight of the selected item
        
        items.reverse()  # Reverse to print the items in the original order
        
        # Print the results
        print(f'The number of items selected: {len(items)}') 
        print(f'Positions Selected: {items}') 
        
        # Loop over the selected item indices to get corresponding weights and values
        selected_weights = [self.weights[i] for i in items] 
        selected_values = [self.values[i] for i in items]
        
        print(f'Weights Selected: {selected_weights}, Total Weights: {total_weight}')

        # Total Values are reinitialized because algorithm sets total values to zero after backtracking
        print(f'Values Selected: {selected_values}, Total Values: {self.table[self.num_items][self.max_weight]}')


class Driver:
    '''
    Create Driver class that initializes the Knapsack class as stated in the assignment
    '''
    def __init__(self, max_weight, weights, values):
        self.knapsack = Knapsack(max_weight, weights, values)
    
    def solve(self):
        self.knapsack.solve()
        self.knapsack.display_solution()


