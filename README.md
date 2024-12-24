# Fault-Tolerant Implementation of the Deutsch-Jozsa Algorithm

This code implements the Deutsch-Jozsa Algorithm in a fault-tolerant manner and has been tested on the Ion Trap QPU [IonQ Aria-1](https://ionq.com/quantum-systems/aria). The implementation leverages several Python packages, including `qiskit`, `qiskit-ionq`, and `qiskit-braket-provider`.

The experiment involves the fault-tolerant implementation of the Deutsch-Jozsa Algorithm, utilizing a small quantum error-detecting code \([[4,2,2]]\).


For more information you can read :

[Fault-tolerant-DJ-Algorithm](https://arxiv.org/abs/2412.04791)
[Gottesman2016](https://arxiv.org/abs/1610.03507), 
[Vuillot2017](https://arxiv.org/abs/1705.08957).


## Organisation

The folder `Bare Circuit Codes`  contains the QASM files and Jupyter notebooks of the bare circuit which are used to run the experiments.
The folder `Encoded Circuit Codes` contains Jupyter notebooks of encoded circuits used in the experiements.
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
