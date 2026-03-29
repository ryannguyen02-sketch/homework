### CS 22B Project - P1 Pure function and Try-Except
### Group Name: <Team member names>

##### Project Assignment to Practice Try-Except Exceptions #####
## For this assignment, you will design and implement a small collection of 
# pure functions related to your team's project. 

## Requirements: Be sure that for each function that you meet the requirements  and include:
# - A clear function name
# - Includes at least one parameter
# - Include a docstring and a return statement
# - Is pure and has no side effects
# - For each function, provide at least 1 test cases (eg assert) to show that it works correctly.

##### Function 1: A decision-making function using conditionals #####
## Write a Python function that takes input data and returns a transformed version.
if calories < 200:
        return "low"
    elif calories <= 300:
        return "medium"
    return "high"


##### Function 2: Re-write Exception Handling #####
## Write a Python function that uses if, elif, and/or else to classify or evaluate something.
def protein_rating(protein):

    if protein < 5:
        return "poor"
    elif protein <= 15:
        return "good"
    return "excellent"




##### Function 3: A function that uses try-except #####
### Write a function that safely handles invalid input and returns a meaningful result without crashing.
def safe_calorie_per_serving(total_calories, servings):

    try:
        total = float(total_calories)
        count = float(servings)
        if count <= 0:
            return "Servings must be greater than 0."
        return total / count
    except ValueError:
        return "Invalid input: please enter numbers only."
    except TypeError:
        return "Invalid input type."

##### Function 4: A function that works with a collection #####
### Write a function that processes a collection (list, tuple, set, or dictionary) and returns a result.
def total_calories(food_calories):
 
    try:
        return sum(food_calories)
    except TypeError:
        return "Invalid input: all items must be numbers."

##### Function 5: A function of your own design #####
### Choose one additional useful function for your project.
def remaining_calories(goal, consumed):
  
    return goal - consumed
