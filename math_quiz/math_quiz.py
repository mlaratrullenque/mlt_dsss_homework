import random


def random_integer(min, max):
    """returns a random integer between a given minimum and maximum
Parameters
----------
min : int
    lower limit
max : int
    upper limit

Returns
-------
random_int : int
    result of the random integer selection between min and max
"""
    random_int = random.randint(min, max)

    return random_int


def random_operation():
    """returns a random operation sign between '+', '-', '*'
    Parameters
    ----------
    None

    Returns
    -------
    random_op : str
        result of the random operation selection between '+', '-', '*'
    """

    random_op = random.choice(['+', '-', '*'])

    return random_op


def create_problem(number1, number2, operation):
    """forms a mathematical operation problem with the given numbers and operation and its answer
    Parameters
    ----------
    number1 : int
        first number given for the problem
    number2 : int
        second number given for the problem

    Returns
    -------
    problem : str
        mathematical operation to be solved
    answer : int
        correct answer for the created mathematical operation
    """


    problem = f"{number1} {operation} {number2}"
    if operation == '+': answer = number1 + number2
    elif operation == '-': answer = number1 - number2
    else: answer = number1 * number2
    return problem, answer 


def math_quiz(number_questions=5):
    """simple math quiz game. It generates random math problems, prompts the user to solve them, 
    and provides feedback on the correctness of their answers. The user earns a point for each correct answer, 
    and the final score is displayed at the end of the game.

    Parameters
    ----------
    number_questions : int, optional
        The number of math problems to present to the user. Default is 5.


    Returns
    -------
    final_score : float
        final score obtained by user over 10 points 
    
    """

    #initialize the ontained points at 0
    sum_points = 0

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(number_questions):
        #select 2 random numbers and a random operation
        number1 = random_integer(1, 10); number2 = random_integer(1, 5); operation = random_operation() #ojo al tipo de datos en number2 integer?

        #create a problem with those numbers and obtain the answer
        problem, answer = create_problem(number1, number2, operation)
        print(f"\nQuestion: {problem}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        #compare the user's answer to the correct answer and if sum the corresponding points
        if useranswer == answer:
            print("Correct! You earned a point.")
            sum_points += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {answer}.")
    
    #final score is obtained over 10 points
    final_score = (sum_points/number_questions) * 10
    print(f"\nGame over! Your score is: {final_score} /10 ")

if __name__ == "__main__":
    math_quiz()
