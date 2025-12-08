#part 1 and part 2 required
#import required libraries0
import numpy as np
import matplotlib.pyplot as plt
import time

plt.style.use('seaborn-v0_8-darkgrid') #make plots look nice

#set random seed for reproducibility
np.random.seed(42)

#print("lab enviroment ready!")
#print(f'NumPy version: {np.__version__}')

def exercise_1_1():
    '''
    print("="*50)
    print("Exercise 1.1: Array Creation Methods")
    print("="*50)
    '''
    array_range = np.arange(21)
    print(array_range)