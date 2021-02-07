import numpy as np
import argparse
import randoms
import quantum_random
import functions
import warnings


warnings.filterwarnings("ignore", category=DeprecationWarning)

def parse_input():
    parser = argparse.ArgumentParser()
    parser.add_argument('min',help="Sets the minimum value in the range for simulation",type=float)
    parser.add_argument('max',help="Sts the maximum value in the range for the simulation",type=float)
    parser.add_argument('mode',help="selects whether to run on 'quantum' or 'numpy' defaults to numpy")
    parser.add_argument('distribution',help="probability distibution to be used fo random variables, options are: 'uniform','normal','log-normal'. Dafaults to :'uniform'", default='uniform')
    parser.add_argument('--apitoken',help="API token for if remote is selected")
    parser.add_argument('--remote',help="run on qasm simulator(False) or IBM cloud(True)")
    args=parser.parse_args()
    return args



def crude_monte_carlo(lower_bound, upper_bound,num_samples=5000,mode="numpy",remote='False',distribution='uniform',apitoken='0000'):
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
            x = randoms.get_rand_number(lower_bound, upper_bound,distribution)
        elif mode=="quantum":
            x=quantum_random.get_rand_number(lower_bound,upper_bound,remote,distribution,apitoken)
        sum_of_samples += functions.f_of_x(x)
    
    return (upper_bound - lower_bound) * float(sum_of_samples/num_samples)


if __name__=="__main__":
    args=parse_input()
    print(crude_monte_carlo(args.min,args.max,500,args.mode,args.remote,args.distribution,args.apitoken))
    #print("numpy",crude_monte_carlo(50,mode="numpy"))
    #print("quantum",crude_monte_carlo(50,mode="quantum"))
 