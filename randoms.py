import random
import warnings

warnings.filterwarnings("ignore")


#TODO implement both functions here, quantum and numpy

def get_rand_number(min_value, max_value,distribution):
    """
    This function gets a random number from a uniform distribution between
    the two input values [min_value, max_value] inclusively
    Args:
    - min_value (float)
    - max_value (float)
    Return:
    - Random number between this range (float)
    """
    range = max_value - min_value
    if distribution=='uniform':
        choice = random.uniform(0,1)
    elif distribution=='normal':
        choice=random.normal()
    elif distribution=='lognormal':
        choice=random.lognormal()
    return min_value + range*choice


