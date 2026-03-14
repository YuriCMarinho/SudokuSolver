# SudokuSolver

A simple **Sudoku solver with a graphical interface (Tkinter)** that uses **Prolog (CLP(FD))** to solve the puzzle.  
The Python app collects the grid input and delegates the solving to a Prolog constraint model.

## Features
- 9×9 Sudoku GUI built with **Tkinter**
- Solving powered by **Prolog constraints** (`library(clpfd)`)
- Fill in known numbers and click **Resolver** to complete the grid
- Shows a message if **no solution** is found

## How it works (high level)
- `prolog.py` creates a Tkinter 9×9 grid of inputs.
- Empty cells are passed to Prolog as variables via **PySWIP**.
- The Prolog program applies Sudoku constraints:
  - all rows distinct
  - all columns distinct (via `transpose/2`)
  - all 3×3 blocks distinct
  - domain 1..9 and labeling to find a solution

## Project structure
- `prolog.py` — Tkinter GUI + Python/Prolog bridge (PySWIP)
- `sudoku.pl` — Prolog Sudoku constraints using `clpfd`

## Requirements
- Python 3.x
- SWI-Prolog installed
- Python package: `pyswip`

## Installation
1) Clone the repository:
```bash
git clone https://github.com/YuriCMarinho/SudokuSolver.git
cd SudokuSolver
