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


## Task 11852cab.json

![11852cab.json](https://github.com/pturdaibay/ARC/blob/master/data/src/grid-printouts/11852cab.json.png "Task 11852cab.json")

This task will process a grid and identify the missing pieces for a specific shape that must be  the output, this shape is a square of non-adjacent elements, once the elements on the grid are detected, the missing pieces must be placed and coloured appropriately, before returning the grid.

I had initially used the shapes function in solutils to identify the pieces on the grid, adjacent via diagonal touch, this worked for training sets 1 and 2, however for the 3rd it failed, as it can be seen on the image above, training grid 3 has pieces that don’t touch even diagonally, therefore I used another method to just select all coloured elements on the grid (solutils.get_all_coloured).

Once the shape elements are detected, I proceeded to identify the centre, corner, middle ring, and side elements; finally, selecting the colour was based on other elements of the same part, for example for a missing corner, if there are other corners then use the colour they have, otherwise use the colour of the centre element (as per training grid 1).


## Task c909285e.json

![c909285e.json](https://github.com/pturdaibay/ARC/blob/master/data/src/grid-printouts/c909285e.json.png "Task c909285e.json")

The solution for this task relies in finding that square/rectangle that is unique due to its colour, and then returning a grid that is formed by all the elements constrained by that frame, itself included.

I also used the shapes function here, for elements touching on their sides and with the same colour. Once that was done, it was simply find the shape that had the unique colour, I created the function solutils.find_unique_c909285e for this, it returns a list of indexes of shapes where its colour is unique (no other shape shares that colour), in theory this list should only contain one element, so no further validation is done if more than one shape have a unique colour. It is expected that only one shape will comply, and that shape will be an encapsulating frame.

The corners of the frame are calculated using the index of the shape returned, and with those then the output grid is extracted from the input grid and returned.


## Summary

I used basic Python libraries to solve the tasks, creating a package file solutils.py that contains functions used across all 3 tasks, and also some task-specific functions. The most useful function was shapes, which finds shapes on a given grid, based on colour (or not), and how the pieces of the shape connect together. Any element on the grid that had a value of 0 was considered not coloured and not part of any shape.

I believe in order to solve tasks in ARC, shape detection and importance (which shapes are meaningful to the task) is one of the most interesting and probably complex parts.

All 3 tasks shared features like loading the task json file, processing the train and test data using solve, and printing out the resulting grid.

I also tried to keep solve simple to be easier to view the main steps used to solve the task, most of the code in the package.

Although I created a few task specific functions, I believe there’s room to make those shareable by other tasks in ARC, given that many tasks will share properties with others across the whole set.
