import numpy as np
from qiskit.circuit.library import TwoLocal

def normalize_amplitude(vec):
    vec = np.array(vec, dtype=np.complex128)

    if np.isnan(vec).any():
        raise ValueError("❌ Input vector contains NaN before normalization.")

    norm = np.linalg.norm(vec)
    if norm == 0 or np.isnan(norm):
        raise ValueError("❌ Zero or NaN norm encountered.")

    vec = vec / norm
    power_sum = np.sum(np.abs(vec)**2)

    if not np.isclose(power_sum, 1.0, atol=1e-10):
        vec = vec / np.sqrt(power_sum)

    if np.isnan(vec).any():
        raise ValueError("❌ NaNs appeared after normalization.")

    return vec

def build_encoder(num_qubits=4, reps=1):
    return TwoLocal(
        num_qubits=num_qubits,
        rotation_blocks="ry",
        entanglement_blocks="cz",
        entanglement='full',
        reps=reps,
        insert_barriers=True
    )
