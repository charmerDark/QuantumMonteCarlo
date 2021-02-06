from qiskit.providers.ibmq import least_busy
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute, BasicAer

def bit_from_counts(counts):
    return [k for k, v in counts.items() if v == 1][0]
def choice(remote=False):
    bits=''
    qc=QuantumCircuit(10,10)
    qc.h(range(10))
    for i in range(10):
        qc.measure(i,i)
    if remote:
                IBMQ.load_account()
                provider=IBMQ.get_provider(hub='ibm-q', group='open', project='main') 
                backend = least_busy(provider.backends(filters=lambda x: x.configuration().n_qubits >= MAX_QUBITS and
                                    not x.configuration().simulator and x.status().operational==True))
                print("least busy backend: ",backend)
    else:
                backend=BasicAer.get_backend('qasm_simulator')
    job_sim = execute(qc, backend, shots=1)
    sim_result = job_sim.result()
    counts = sim_result.get_counts(qc)
    bits += bit_from_counts(counts)
    result= int(bits,2)
    if result>=1000:
        result=choice()
        return result
    val=result/1000
    return val


def get_rand_number(min_value, max_value,remote=False):
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
    var=choice(remote)
    return min_value + range*var

if __name__=="__main__":
    for i in range(10):
        print(get_rand_number(1,100))
        print("######")