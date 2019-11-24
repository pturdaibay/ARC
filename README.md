# Solving 3 tasks from "The Abstraction and Reasoning Corpus (ARC)"

This repository contains solutions for 3 specific tasks from [ARC](https://github.com/fchollet/ARC), taken from its data/training directory.

Task files solved:
- 67385a82.json
- 11852cab.json
- c909285e.json

## Task file format

The `data` directory contains two subdirectories:

- `data/training`: contains the task files for training (400 tasks). Use these to prototype your algorithm or to train your algorithm to acquire ARC-relevant cognitive priors.
- `data/evaluation`: contains the task files for evaluation (400 tasks). Use these to evaluate your final algorithm. To ensure fair evaluation results, do not leak information from the evaluation set into your algorithm (e.g. by looking at the evaluation tasks yourself during development, or by repeatedly modifying an algorithm while using its evaluation score as feedback).

The tasks are stored in JSON format. Each task JSON file contains a dictionary with two fields:

- `"train"`: demonstration input/output pairs. It is a list of "pairs" (typically 3 pairs).
- `"test"`: test input/output pairs. It is a list of "pairs" (typically 1 pair).

A "pair" is a dictionary with two fields:

- `"input"`: the input "grid" for the pair.
- `"output"`: the output "grid" for the pair.

A "grid" is a rectangular matrix (list of lists) of integers between 0 and 9 (inclusive). The smallest possible grid size is 1x1 and the largest is 30x30.

When looking at a task, a test-taker has access to inputs & outputs of the demonstration pairs, plus the input(s) of the test pair(s). The goal is to construct the output grid(s) corresponding to the test input grid(s), using 3 trials for each test input. "Constructing the output grid" involves picking the height and width of the output grid, then filling each cell in the grid with a symbol (integer between 0 and 9, which are visualized as colours). Only *exact* solutions (all cells match the expected answer) can be said to be correct.


## Task 67385a82.json

![67385a82.json](https://github.com/pturdaibay/ARC/blob/master/data/src/grid-printouts/67385a82.json.png "Task 67385a82.json")

This task will colour blue all shapes that are larger than one position on the grid, where the shapes are formed by multiple adjacent positions touching on their sides with the same colour.

`solve` will extract all the shapes from the grid, identify which are formed by more than one position, and then colour them and return the updated grid. `solutils.shapes` is used to extract all the shapes, then a loop is used to check and colour those that are larger than one element on the grid.

## Task
