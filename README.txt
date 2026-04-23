🗺️ Map Coloring Problem Solver (CSP)
Problem Description

This project solves the Map Coloring Problem using a Constraint Satisfaction Problem (CSP) approach.

The goal is to assign colors to different regions of a map such that:

No two adjacent regions have the same color
The number of colors used is limited

Example:
Color regions A, B, C, D, E such that neighboring regions are differently colored.

Algorithm Used

Constraint Satisfaction Problem (CSP) using Backtracking Algorithm.

CSP Representation
Variables: Regions of the map (e.g., A, B, C, D, E)
Domain: Available colors (e.g., Red, Green, Blue)
Constraints:
Adjacent regions must not have the same color
Each region must be assigned exactly one color
Execution Steps
Define the map as a graph (adjacency list)
Assign a list of available colors
Select a region (variable)
Try assigning a color from the domain
Check constraints (no same color for neighbors)
If valid, move to next region
If not valid, backtrack and try another color
Repeat until all regions are colored
Features
GUI-based interface using Tkinter
Visual representation of regions
One-click solution using backtracking
Displays colored map as output
Handles cases where no solution exists
How to Run

Run the following command:

python map_gui.py

Click Solve Map Coloring to generate the solution.

Sample Output
A → Red  
B → Green  
C → Blue  
D → Green  
E → Red  

(Displayed visually in GUI with colored regions)

Project Structure
MapColoring/
│
├── map_solver.py
├── map_gui.py
└── README.md

AUTHOR
NAME : PORANI SRI S REG NO : RA2411026050139
