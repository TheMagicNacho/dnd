import qiskit
from qiskit import IBMQ
import math
import struct
# THIS PART IS THE QUANTUM SHIT SO PUCKER YOUR BUTTHOLES
_backend = qiskit.BasicAer.get_backend('qasm_simulator')
_circuit = None
_bitCache = ''

def setqbits(n):
    global _circuit
    qr = qiskit.QuantumRegister(n)
    cr = qiskit.ClassicalRegister(n)
    _circuit = qiskit.QuantumCircuit(qr, cr)
    _circuit.h(qr) # Apply Hadamard gate to qubits
    _circuit.measure(qr,cr) # Collapses qubit to either 1 or 0 w/ equal prob.

setqbits(3) # Default Circuit is 3 Qubits

def set_backend(b = 'qasm_simulator'):
    global _backend
    if b == 'ibmqx4' or b == 'ibmqx5':
        _backend = IBMQ.get_backend(b)
        setqbits(5)
    elif b == 'ibmq_16_melbourne':
        _backend = IBMQ.get_backend(b)
        setqbits(16)
    elif b == 'ibmq_qasm_simulator':
        _backend = IBMQ.get_backend(b)
        setqbits(32)
    else:
        _backend = qiskit.BasicAer.get_backend('qasm_simulator')
        setqbits(8)

# Strips QISKit output to just a bitstring.
def bitcount(counts):
    return [k for k, v in counts.items() if v == 1][0]

# Populates the bitCache with at least n more bits.
def _request_bits(n):
    global _bitCache
    iterations = math.ceil(n/_circuit.width())
    for _ in range(iterations):
        # Create new job and run the quantum circuit
        job = qiskit.execute(_circuit, _backend, shots=1)
        _bitCache += bitcount(job.result().get_counts())

# Returns a random n-bit string by popping n bits from bitCache.
def bitstring(n):
    global _bitCache
    if len(_bitCache) < n:
        _request_bits(n-len(_bitCache))
    bitString = _bitCache[0:n]
    _bitCache = _bitCache[n:]
    return bitString

# Returns a random integer between and including [min, max].
# Running time is probabalistic but complexity is still O(n)
def randint(min,max):
    delta = max-min
    n = math.floor(math.log(delta,2))+1
    result = int(bitstring(n),2)
    while(result > delta):
        result = int(bitstring(n),2)
    return result+min

# this is the part where users import and use the program

def main():
  while True:
    prompt_user()

def prompt_user():
# grab user deffinitions
    try:
        dice_number = input("How many dice? [default 1] ")
        xdice_number = int(dice_number)
    except:
        xdice_number = int(1)

    try:
        sides = input("How many sides? [default 20] ")
        xside = int(sides)
    except:
        xside = int(20)

    try:
        mod = input("modifying number? ['enter' for no modifyer] ")
        xmod = int(mod)
    except:
        xmod = int(0)

# generate adaptive list of dice rolls from user
    roll_list = []
    for i in range(xdice_number):
        roll_list.append(randint(1, xside))  # append to our_list

# conduct required math
    final = sum(roll_list) + xmod

# Print the outputs
    print("Your Quantum Dice Rolls:", roll_list )
    print("You modified by:", xmod)
    print("\n")
    print("YOUR QUANTUM COMPUTED FINAL:", final)

# Keep the fun going or pussy out
    again = input("Roll again! (Or else type 'n' to quit)\n ")

    if again.lower() == "n":
        exit()

if __name__ == '__main__': main()
