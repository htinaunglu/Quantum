from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.compiler import transpile, assemble
xor_circuit = QuantumCircuit(2)

# Put control qubit (qubit 0) in state 1
xor_circuit.x(0)

# apply CNOT (controlled-NOT) gate; control qubit is qubit 0, target qubit is qubit 1
xor_circuit.cx(0, 1)

print(xor_circuit.draw())

# Measure both qubits
xor_circuit.measure_all()

# Execute the circuit
xor_backend = AerSimulator()
compiled_xor_circuit = transpile(xor_circuit, xor_backend)
xor_result = xor_backend.run(compiled_xor_circuit).result()
xor_counts = xor_result.get_counts(xor_circuit)
print(f"Measurement results: {xor_counts}")
