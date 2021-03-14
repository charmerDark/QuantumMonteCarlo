## Monte Carlo Simulator for Commision Modelling with Quantum Random Number Generator

The project aims to set up a simple monte carlo simutor that models univariate functions with the help of a quantum random generator. The code is set up to allow the user to select between the default numpy RNG or a QRNG using the IBMQ quantum computing network.

### Development plan
<ul>
<li> Setup simple Monte Carlo Simulator (MCS) on python[DONE] </li>
<li>Setp simple QRNG[DONE]</li>
<li>link QRNG to MCS{DONE}</li>
<li>enable QRNG with probablity distributions<[DONE]</li>
  <li>Study effects of QRNG on montecarlo accuracy and efficieny</li>
</ul>

### Sources
<ul>
<li>https://towardsdatascience.com/monte-carlo-simulations-with-python-part-1-f5627b7d60b0</li>
<li>https://pbpython.com/monte-carlo.html</li>
<li>https://medium.com/qiskit/programming-a-quantum-computer-generating-true-random-numbers-7dd631ef10a1</li>
<li>https://quantumcomputinguk.org/tutorials/modelling-probability-distributions-in-qiskit</li>

</ul>

### Instructions for use
<ol>
<li> first time users can use python3 -m pip install -r requirements.txt </li>  
<li>Enter target function as a function of x in the functions.py in python language </li>
<li>call  montecarlo.py --h for help on how to use the simulator</li>
</ol>
