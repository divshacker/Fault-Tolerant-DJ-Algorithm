# Fault-Tolerant Implementation of the Deutsch-Jozsa Algorithm

Here, we provide the code and experimental data for a small experiment comparing fault-tolerant and non-fault-tolerant implementations of the Deutsch-Jozsa Algorithm reported in [Singh2024](https://arxiv.org/abs/2412.04791). We implemented the Deutsch-Josza algorithm in both a fault-tolerant manner using the [[4,2,2]] quantum error-detecting code and a non-fault-tolerant manner on the Ion Trap QPU [IonQ Aria-1](https://ionq.com/quantum-systems/aria). 

The implementation leverages several Python packages, including `qiskit`, `qiskit-ionq`, and `qiskit-braket-provider`.

For any questions, please contact one of the authors of [Singh2024](https://arxiv.org/abs/2412.04791).

Some References:
[Gottesman2016](https://arxiv.org/abs/1610.03507), 
[Vuillot2017](https://arxiv.org/abs/1705.08957).
[Singh2024](https://arxiv.org/abs/2412.04791)

## Organisation

The folder `Bare Circuit Codes`  contains the QASM files and Jupyter notebooks of the bare (non-fault-tolerant) circuits implementing the Deutsch-Josza algorithm on all four oracles.
The folder `Encoded Circuit Codes` contains Jupyter notebooks of encoded (fault-tolerant) circuits implementing the Deutsch-Josza algorithm on all four oracles.
The folder `Experimental/Bare Circuit Results` and `Experimental/Encoded Circuit Results` contains `.json` files which have all the exact counts of results of the experiments.

```
├── Bare circuit codes
│   ├── bare_1.qasm
│   ├── bare_2.qasm
│   ├── bare_3.qasm
│   ├── bare_4.qasm
│   ├── bare_circuit_1.ipynb
│   ├── bare_circuit_2.ipynb
│   ├── bare_circuit_3.ipynb
│   └── bare_circuit_4.ipynb
├── Encoded circuit codes
│   ├── encoded_circuit_1.ipynb
│   ├── encoded_circuit_2.ipynb
│   ├── encoded_circuit_3.ipynb
│   └── encoded_circuit_4.ipynb
├── Experimental Results
│   ├── Bare Circuit Results
│   │   ├── bare_deutsch_d1.json
│   │   ├── bare_deutsch_d2.json
│   │   ├── bare_deutsch_d3.json
│   │   └── bare_deutsch_d4.json
│   └── Encoded Circuit Results
│       ├── encoded_deutsch_d1.json
│       ├── encoded_deutsch_d2.json
│       ├── encoded_deutsch_d3.json
│       └── encoded_deutsch_d4.json
└── README.md
```
