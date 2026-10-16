# Fault-Tolerant Implementation of the Deutsch-Jozsa Algorithm

Here, we provide the code and experimental data for a small experiment comparing fault-tolerant and non-fault-tolerant implementations of the Deutsch-Jozsa Algorithm reported in [Singh2024](https://arxiv.org/abs/2412.04791). We implemented the Deutsch-Jozsa algorithm in both a fault-tolerant manner using the [[4,2,2]] quantum error-detecting code and a non-fault-tolerant manner on the Ion Trap QPU [IonQ Aria-1](https://ionq.com/quantum-systems/aria).

The implementation leverages several Python packages, including `qiskit`, `qiskit-ionq`, and `qiskit-braket-provider`.

For any questions, please contact one of the authors of [Singh2024](https://arxiv.org/abs/2412.04791).

Some References:
[Gottesman2016](https://arxiv.org/abs/1610.03507),
[Vuillot2017](https://arxiv.org/abs/1705.08957),
[Singh2024](https://arxiv.org/abs/2412.04791)

## Organisation

The folder `Bare circuit codes` contains the QASM files and Jupyter notebooks of the bare (non-fault-tolerant) circuits implementing the Deutsch-Jozsa algorithm on all four oracles.

The folder `Encoded circuit codes` contains Jupyter notebooks of the encoded (fault-tolerant) circuits implementing the Deutsch-Jozsa algorithm on all four oracles.

The folders `Experimental-Results/Bare Circuit Results` and `Experimental-Results/Encoded Circuit Results` contain `.json` files with the exact counts of the results of the experiments.

The folder `Entangled_States_Results` contains the results of the entangled-state experiments (circuits A to H). See the section below.

```
├── Bare circuit codes
│   ├── bare_1.qasm
│   ├── bare_2.qasm
│   ├── bare_3.qasm
│   ├── bare_4.qasm
│   ├── bare_circuit_1.ipynb
│   ├── bare_circuit_2.ipynb
│   ├── bare_circuit_3.ipynb
│   └── bare_circuit_4.ipynb
├── Encoded circuit codes
│   ├── encoded_circuit_1.ipynb
│   ├── encoded_circuit_2.ipynb
│   ├── encoded_circuit_3.ipynb
│   └── encoded_circuit_4.ipynb
├── Entangled_States_Results
│   ├── Bare_Circuit_A.json
│   ├── Bare_Circuit_B.json
│   ├── Bare_Circuit_C.json
│   ├── Bare_Circuit_D.json
│   ├── Bare_Circuit_E.json
│   ├── Bare_Circuit_F.json
│   ├── Bare_Circuit_G.json
│   ├── Bare_Circuit_H.json
│   ├── Encoded_Circuit_A.json
│   ├── Encoded_Circuit_B.json
│   ├── Encoded_Circuit_C.json
│   ├── Encoded_Circuit_D.json
│   ├── Encoded_Circuit_E.json
│   ├── Encoded_Circuit_F.json
│   ├── Encoded_Circuit_G.json
│   └── Encoded_Circuit_H.json
├── Experimental-Results
│   ├── Bare Circuit Results
│   │   ├── bare_deutsch_d1.json
│   │   ├── bare_deutsch_d2.json
│   │   ├── bare_deutsch_d3.json
│   │   └── bare_deutsch_d4.json
│   └── Encoded Circuit Results
│       ├── encoded_deutsch_d1.json
│       ├── encoded_deutsch_d2.json
│       ├── encoded_deutsch_d3.json
│       └── encoded_deutsch_d4.json
└── README.md
```

## Entangled-States Data (Circuits A to H)

The folder `Entangled_States_Results` contains the raw results for the entangled-state experiments in Appendix B of [Singh2024](https://arxiv.org/abs/2412.04791). Eight two-qubit entangled states (circuits A to H) were prepared in a bare version and in a fault-tolerant version using the [[4,2,2]] code, giving 16 files: `Bare_Circuit_A.json` to `Bare_Circuit_H.json` and `Encoded_Circuit_A.json` to `Encoded_Circuit_H.json`.

The encoded circuits use the "conventional" fault-tolerant dictionary of [Vuillot2017](https://arxiv.org/abs/1705.08957), not the dictionary used for the Deutsch-Jozsa circuits. All runs used 4096 shots on IonQ Aria-1 through Amazon Braket.

The states prepared are:

- **A:** start from `(|00> + |11>)/sqrt(2)`, apply `I x I`, final state `(|00> + |11>)/sqrt(2)`
- **B:** start from `(|00> + |11>)/sqrt(2)`, apply `I x Z`, final state `(|00> - |11>)/sqrt(2)`
- **C:** start from `(|00> + |11>)/sqrt(2)`, apply `X x I`, final state `(|10> + |01>)/sqrt(2)`
- **D:** start from `(|00> + |11>)/sqrt(2)`, apply `I x ZX`, final state `(|10> - |01>)/sqrt(2)`
- **E:** start from `|00>`, apply `CZ . H x H`, final state `(|00> + |01> + |10> - |11>)/2`
- **F:** start from `|00>`, apply `CZ . Z x I . H x H`, final state `(|00> - |01> + |10> + |11>)/2`
- **G:** start from `|00>`, apply `CZ . I x Z . H x H`, final state `(|00> + |01> - |10> + |11>)/2`
- **H:** start from `|00>`, apply `X x I . CZ . H x H . X x I`, final state `(|00> - |01> - |10> - |11>)/2`

The encoded circuits for E to H measure five qubits (32 outcomes) instead of four. See Table VIII of the paper for the statistical distances and post-selection ratios.

**Compilation note.** Encoded circuits G and H (`Encoded_Circuit_G.json` and `Encoded_Circuit_H.json`) were run without verbatim compilation, so Braket may have recompiled them. All other encoded circuits were run as verbatim native-gate circuits. Results for G and H are therefore not directly comparable to the rest.

**File format.** Each file is a Braket task result in JSON. The field `measurementProbabilities` maps each measured bitstring to its observed probability. Multiply by 4096 to get raw counts. `measuredQubits` lists the measured qubits, and the submitted OpenQASM program is stored under `additionalMetadata`.

## Citation

If you use this code or data, please cite the paper:

> Divyanshu Singh and Shiroman Prakash, "Fault-Tolerant Implementation of the Deutsch-Jozsa Algorithm", [arXiv:2412.04791](https://arxiv.org/abs/2412.04791).

```bibtex
@misc{Singh2024,
  author        = {Singh, Divyanshu and Prakash, Shiroman},
  title         = {Fault-Tolerant Implementation of the Deutsch-Jozsa Algorithm},
  year          = {2024},
  eprint        = {2412.04791},
  archivePrefix = {arXiv},
  primaryClass  = {quant-ph},
  url           = {https://arxiv.org/abs/2412.04791}
}
```

## License

This repository is released under the [MIT License](LICENSE.md).
