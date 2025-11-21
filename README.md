## 📘 Structured Git/GitHub usage — OBI Programming Project

The goal of this project is to showcase solutions to OBI (Brazilian Informatics Olympiad) problems, computer-related tasks, and random chess challenges, all implemented in Python. It also serves as an example of using Git for project and repository management.
______________________________________
## 📑 Table of Contents

- [About the Project](#-about-the-project)

- [Problem Description](#-problem-description)

- [OBI Context](#-obi-context)

- [Approach & Solution](#-approach--solution)

- [Algorithm Explanation](#-algorithm-explanation)

- [Complexity Analysis](#️-complexity-analysis)

- [How to Run](#️-how-to-run)

- [Input & Output Examples](#-input--output-examples)

- [Project Structure](#-project-structure)

- [Testing](#-testing)

- [Git Workflow](#-git-workflow)

- [References](#-references)

- [License](#-license)
_______________________________________
## 📘 About the Project

    This repository contains the source code and explanation for solving the OBI problem “Computer” (year 2019, phase 3) and “Chess” (year 2019, phase 3).
______________________________________

## 📝 Problem Description

Summarize the problem as described in the OBI statement.

- What is the task?

- What are the inputs/outputs?

- What constraints does it impose?
```bash
PS C:\Users\f1aud\Project-codiname-IC> git pull
error: You have not concluded your merge (MERGE_HEAD exists).
hint: Please, commit your changes before merging.
fatal: Exiting because of unfinished merge.
```
---
## Problem 1 Computer

### OBI Memory Instructions Simulator

A large company is designing a new computer architecture that supports two efficient special addition instructions. The computer contains **N memory positions**, indexed from **1 to N**, and each position stores a non‑negative integer. Initially, all memory positions contain zero.

## 📌 Special Addition Instructions

### **FRENTE i V**

Given an address `i` (where `1 ≤ i ≤ N`) and a positive value `V`, the computer must:

* Add `V` to position `i`,
* Add `V-1` to position `i+1`,
* Add `V-2` to position `i+2`,
* And so on...

This continues while the value being added is greater than zero **and** the memory position does not exceed `N`.

### **TRÁS i V**

Given an address `i` (where `1 ≤ i ≤ N`) and a positive value `V`, the computer must:

* Add `V` to position `i`,
* Add `V-1` to position `i-1`,
* Add `V-2` to position `i-2`,
* And so forth...

This continues while the value being added is greater than zero **and** the memory position is at least `1`.

## 📘 Example (N = 16)

Below is an example execution sequence:

```
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
FRENTE 4 8

0 0 0 8 7 6 5 4 3 2 1 0 0 0 0 0
TRÁS 16 3

0 0 0 8 7 6 5 4 3 2 1 0 0 1 2 3
TRÁS 2 12

11 12 0 8 7 6 5 4 3 2 1 0 0 1 2 3
FRENTE 8 7

11 12 0 8 7 6 5 11 9 7 5 3 2 2 2 3
```

## 🖨️ Print Instruction

### **IMPRIME i**

This instruction prints the current value stored at memory position `i`.

## 🎯 Objective

Given `N` and a sequence of `M` instructions, your program must:

* Process each instruction in order,
* And for every `IMPRIME i` instruction,
* Output the value at memory position `i` **at that moment**.

## 🧩 Notes

* All memory positions start with value **0**.
* Values never become negative.
* The instructions may overlap in their effects.

## 📥 Input

The first line of input contains two integers `N` and `M`, representing the number of memory positions and the number of instructions, respectively.

Each of the next `M` lines contains one instruction in one of the following formats:

* `1 I V` — represents **FRENTE I V**
* `2 I V` — represents **TRÁS I V**
* `3 I` — represents **IMPRIME I**

## 📤 Output

For every instruction of type `IMPRIME I`, the program must output a line containing the integer value currently stored at memory position `I` at the moment the instruction is executed.

## 🔒 Constraints

* `1 ≤ N ≤ 200000`
* `1 ≤ M ≤ 200000`
* `1 ≤ I ≤ N`
* `1 ≤ V ≤ 200000`
* At least one instruction will be of type `3` (IMPRIME)

## 🛠️ Possible Extensions

* Implementing an optimized solution using prefix differences.
* Adding validation for instruction formats.
* Supporting batch execution and benchmarking.

[link](https://olimpiada.ic.unicamp.br/pratique/pu/2019/f3/computador/) the official Site.
---
_______________________________________
## Problem 2 Chess

### Chess960 Simplified Variant — Valid Starting Positions

Fischer Random Chess, or **Chess960**, is a chess variant that follows all the traditional rules of Chess with one exception: the initial arrangement of the pieces is randomized before play begins. The pieces on the back rank may appear in any order as long as two constraints are met:

* The king must be placed between the two rooks.
* The two bishops must occupy opposite-colored squares.

As the name suggests, this leads to exactly **960 valid starting positions**.

In this problem, we consider a much simpler variant. The size of the board is no longer fixed. For any board dimension `N`, the first row contains only three types of pieces:

* King (exactly one)
* Rook (zero, one, or two)
* Pawn (all remaining positions)

If there are **two rooks**, the king must be placed **between** them. The number of pawns is equal to the board dimension minus the number of other pieces. Below is an example of a valid starting position for `N = 8`.

## 📥 Input

The input consists of a single line containing two integers:

* `N` — the board dimension
* `T` — the number of rooks (0 to 2)

## 📤 Output

Your program must output a single integer representing the number of valid starting positions.

## 🔒 Constraints

* `2 ≤ N ≤ 1000`
* `0 ≤ T ≤ 2`

[link](https://olimpiada.ic.unicamp.br/pratique/pu/2019/f3/xadrez/) the official Site.
_______________________________________
_______________________________________
## 🏅 OBI Context

Add contextual information:

- OBI category: Programação Nível Sênior

- Phase: Third

- Key topics covered (Ordering, dynamic programming, simulation)
_______________________________________
## 🔍 Approach & Solution

Explain your strategy to solve the problem:

- Summary of thought process

- Why this approach works

- Alternative solutions (if relevant)


_______________________________________
## 📐 Algorithm Explanation

A more detailed section:

- Pseudocode

- Step-by-step description

- Important edge cases considered

Example snippet:

1. Read N
2. For each value…
3. Apply greedy rule…
4. Output result
_______________________________________
## ⏱️ Complexity Analysis

State time and memory complexity:

```time
Time Complexity: O(N log N)
Memory Usage: O(N)
```

If needed, explain why this fits the constraints.
_______________________________________
## ▶️ How to Run

Requirements

- Language (Python)

- Version requirements (Python 3.10…)

### Running the program
    
- In Python
    ```P
    C:/Users/$user/AppData/Local/Programs/Python/Python314/python.exe c:/Users/$user/Project-codiname-IC/project-computer/src/main.py
    ```
_______________________________________
## 📥 Input & Output Examples

- Example 1; Computer

Input:
```I
tamanhoMemoria = 16
instrucoes = [
    (1, 4, 8),   # FRENTE 4 8
    (2, 16, 3),  # TRÁS 16 3
    (2, 2, 12),  # TRÁS 2 12
    (1, 8, 7),   # FRENTE 8 7
    (3, 4),      # IMPRIME 4
    (3, 14),     # IMPRIME 14
    (3, 1)       # IMPRIME 1
]
```
Output:
```O
8
2
11
```
- Example 2; Chess

Input:
```I
8 #Posição da casa 1#Nº da Peça; Torre
```
Output:
``` O
56 #Combinações possíveis
```
________________________________________
## 📁 Project Structure

- Example structure:

```repo
project/
 ├── docs/
 │    └── info.rst
 ├── src/
 │    └── main.py
 ├── test/
 │    └── input.txt
 │    └── output.txt
 │    └── expected.txt
 ├── README.md
 └── LICENSE
```

________________________________________
## 🧪 Testing

Explain how to test the solution manually or automatically.

Example:
```exp
./test/input1.txt
```
________________________________________
## 📘 Git Workflow

- Clone repository
```clone
git clone https://github.com/cost-12/Project-codiname-IC.git
cd Project-codiname-IC
```

- Inicicialized repository
```init
git init
```

-  Adicioned informations
```add
git add .
```

- Commit informations
```commit
git commit -m "version"
```

- Upload informations commit
```push
git push -u origin main (first time)
```
________________________________________
## 📚 References

- Official [OBI](https://olimpiada.ic.unicamp.br/pratique/pu/) website
________________________________________
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)                                       | `![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)`                                         |
________________________________________
![Visual Studio](https://img.shields.io/badge/Visual%20Studio-5C2D91.svg?style=for-the-badge&logo=visual-studio&logoColor=white)                  | `![Visual Studio](https://img.shields.io/badge/Visual%20Studio-5C2D91.svg?style=for-the-badge&logo=visual-studio&logoColor=white)`                  |
________________________________________
## 📄 License

- [Unlicense license](https://unlicense.org)
---
[(Back to top)](#table-of-contents)