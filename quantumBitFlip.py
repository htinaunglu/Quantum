from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.compiler import transpile, assemble

# first, create the new quantum circuit with one qubit in the default starting state (|0>)
circuit = QuantumCircuit(1)

# apply the X gate to the qubit in the 0 index (the first (and only) qubit) to flip the qubit state
circuit.x(0)

# print the circuit so we can see what we just did!
print(circuit.draw())

# add a final measurement step
circuit.measure_all()

# use a simulator backend to run the circuit locally
backend = AerSimulator()
compiled_circuit = transpile(circuit, backend)
result = backend.run(compiled_circuit).result()
counts = result.get_counts(circuit)
print("Measurement results: ", counts)
