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
├── LICENSE.md
├── README.md
└── table3_fig4.py
```

The script `table3_fig4.py` recomputes Table III and Fig. 4 of the paper from the raw counts in `Experimental-Results` (`python table3_fig4.py /path/to/this/repo`; needs `scipy` and `matplotlib`).

## Deutsch-Jozsa Run Details

Each run used 4096 shots on IonQ Aria-1. File `dN` corresponds to oracle N: d1 is `f(x) = 0`, d2 is `f(x) = x`, d3 is `f(x) = 1 ⊕ x`, d4 is `f(x) = 1`.

### Bare circuits (Microsoft Azure Quantum)

The bare circuits (`Bare circuit codes/bare_N.qasm`) were submitted through Microsoft Azure Quantum. The result files are in Azure's `microsoft.quantum-results.v2` format: `Histogram` gives the counts and `Shots` gives the per-shot outcomes. Each `Outcome` is listed as `[c[1], c[0]]`, so the Deutsch-Jozsa output qubit `q[0]` is the second entry.

| Result file | Circuit | Azure job ID | Submitted (UTC) |
|---|---|---|---|
| `bare_deutsch_d1.json` | `bare_1.qasm` | `73595704-a596-11ef-9e85-482ae3b166d5` | 2024-11-18 10:18:27 |
| `bare_deutsch_d2.json` | `bare_2.qasm` | `0b28ab9a-a590-11ef-9797-482ae3b166d5` | 2024-11-18 09:32:35 |
| `bare_deutsch_d3.json` | `bare_3.qasm` | `2fda2c08-a594-11ef-9035-482ae3b166d5` | 2024-11-18 10:02:14 |
| `bare_deutsch_d4.json` | `bare_4.qasm` | `b300b140-a596-11ef-8803-482ae3b166d5` | 2024-11-18 10:20:13 |

The Azure job IDs are time-based (version 1) UUIDs, and the submission times above are the timestamps encoded in them.

### Encoded circuits (Amazon Braket)

The encoded circuits were submitted through Amazon Braket as verbatim native-gate programs with qubit rewiring disabled. Each result file is a Braket task result: the field `measurementProbabilities` maps each bitstring to its observed probability (multiply by 4096 for counts), and the submitted OpenQASM program is stored under `additionalMetadata`. The task ID and times below are copied from `taskMetadata` in each file.

| Result file | Braket quantum task ID | Created (UTC) |
|---|---|---|
| `encoded_deutsch_d1.json` | `b84ef362-b74d-4c7b-9da3-077e94637c1d` | 2024-11-19 06:13:39 |
| `encoded_deutsch_d2.json` | `a16b9fc6-c084-486c-ae67-e138ebadf935` | 2024-11-18 08:15:51 |
| `encoded_deutsch_d3.json` | `5febaf58-0286-4551-8226-58b223f903ed` | 2024-11-16 10:49:06 |
| `encoded_deutsch_d4.json` | `9d531fe9-05d5-4b9e-bdf3-041425c45737` | 2024-11-19 06:26:58 |

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
