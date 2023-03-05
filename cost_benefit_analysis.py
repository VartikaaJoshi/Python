import numpy as np

# Define the benefit and cost categories and their possible range of values
benefits = {
    'B1': [1.1, 2, 2.8], 
    'B2': [8, 12, 14.9], 
    'B3': [1.4, 1.4, 2.2], 
    'B4': [6.5, 9.8, 14.6], 
    'B5': [1.7, 2.4, 3.6], 
    'B6': [0, 1.6, 2.4]
}

costs = {
    'C1': [13.2, 14.2, 19.1], 
    'C2': [3.5, 4.9, 7.4]
}

# Define the number of iterations
n_iterations = 10000

# Perform the simulation for Dam #1
dam1_ratios = []
for i in range(n_iterations):
    # Generate random samples for each benefit and cost category
    samples = {}
    for k, v in benefits.items():
        samples[k] = np.random.triangular(left=v[0], mode=v[1], right=v[2])
    for k, v in costs.items():
        samples[k] = np.random.triangular(left=v[0], mode=v[1], right=v[2])
    
    # Calculate the total benefit and total cost
    total_benefit = sum(samples.values()) - sum([samples[k] for k in costs])
    total_cost = samples['C1'] + samples['C2']
    
    # Calculate the benefit-cost ratio
    ratio = total_benefit / total_cost
    dam1_ratios.append(ratio)

# Perform the simulation for Dam #2
dam2_ratios = []
for i in range(n_iterations):
    # Generate random samples for each benefit and cost category
    samples = {}
    for k, v in benefits.items():
        samples[k] = np.random.triangular(left=v[0], mode=v[1], right=v[2])
    for k, v in costs.items():
        samples[k] = np.random.triangular(left=v[0], mode=v[1], right=v[2])
    
    # Calculate the total benefit and total cost
    total_benefit = sum(samples.values()) - sum([samples[k] for k in costs])
    total_cost 
