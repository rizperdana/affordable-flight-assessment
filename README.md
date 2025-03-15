# Cheapest Flight Finder

## Overview
This project implements a solution to find the cheapest flight with at most `k` stops using Dijkstra's algorithm and a priority queue. The solution is implemented in Python and reads input from a JSON file.

## Features
- Reads flight data from a JSON file
- Uses Dijkstra's algorithm with a priority queue to determine the cheapest flight cost
- Allows specifying a maximum number of stops (`k`)
- Includes unit tests for validation

## File Structure
```
├── main.py              # Implementation of the flight search algorithm
├── test_main.py         # Unit tests for the implementation
├── flight_data.json     # JSON file containing input data
├── requirements.txt     # List of dependencies
├── README.md            # Project documentation
```

## Usage

### 1. Prepare Input Data
Modify `flight_data.json` with the following structure:
```json
{
    "n": 4,
    "flights": [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],
    "src": 0,
    "dst": 3,
    "k": 1
}
```

### 2. Run the Program
```sh
python main.py
```
This will output the cheapest flight cost.

### 3. Run Unit Tests
To verify the implementation:
```sh
python -m unittest test.py
```
