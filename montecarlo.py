import numpy as np
import randoms
import quantum_random
import functions
import warnings


warnings.filterwarnings("ignore", category=DeprecationWarning)
lower_bound=0
upper_bound=5

def crude_monte_carlo(num_samples=5000,mode="quantum"):
    """
    This function performs the Crude Monte Carlo for our
    specific function f(x) on the range x=0 to x=5.
    Notice that this bound is sufficient because f(x)
    approaches 0 at around PI.
    Args:
    - num_samples (float) : number of samples
    Return:
    - Crude Monte Carlo estimation (float)
    
    """
    sum_of_samples = 0
    for i in range(num_samples):
        if mode=="numpy":
            x = randoms.get_rand_number(lower_bound, upper_bound)
        elif mode=="quantum":
            x=quantum_random.get_rand_number(lower_bound,upper_bound,remote=False)
        sum_of_samples += functions.f_of_x(x)
    
    return (upper_bound - lower_bound) * float(sum_of_samples/num_samples)

if __name__=="__main__":
    print("numpy",crude_monte_carlo(50,mode="numpy"))
    print("quantum",crude_monte_carlo(50,mode="quantum"))
 