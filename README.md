# Overview
The following repository contains the solution of the following exercise for [ioet](https://www.ioet.com/) recruitment:

>The company ACME offers their employees the flexibility to work the hours they want. But due to some external circumstances they need to know what employees have been at the office within the same time frame  
>
>The goal of this exercise is to output a table containing pairs of employees and how often they have coincided in the office.  
>
>Input: the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our examples below:  
>
>Example 1:  
>
>INPUT  
RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00- 21:00  
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00  
ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00  
>
>OUTPUT:  
ASTRID-RENE: 2  
ASTRID-ANDRES: 3  
RENE-ANDRES: 2  
>
>Example 2:  
>
>INPUT:  
RENE=MO10:15-12:00,TU10:00-12:00,TH13:00-13:15,SA14:00-18:00,SU20:00-21:00  
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00  
>
>OUTPUT:  
RENE-ASTRID: 3

In this way, the solution in ```main.py``` is composed mainly of two functions: ```order_data``` and ```combinator```. Input data is in ```input.txt```. Finally, the output is displayed in the console according to requirements.

# Architecture

The overview section explains that input data is in a text file but the same directory of ```main.py```.  Below, the explanation of the two functions are presented.

## order_data function
`def order_data(file_name)`

In ```main.py```, the first call is to ```order_data``` function. This function receives the input file name and returns a dictionary with all the splitting information.

### Parameters:

#### file name : string
A string data type with the name of the input file, including the extension.

### Return:

#### office_time : dictionary
The dictionary is composed as follows:  
```{employee_name : {day : [start_time, end_time]}}```.
##### employee_name : string
##### day : string
##### start_time : integer
##### end_time : integer
```start_time``` and ```end_time``` are integers representing the day time in minutes.

## combinator function
`def combinator(office_time)`

This function is the solver of the exercise. The input parameter is the dictionary generated in `order_data`. Taking this data, the `combinator` applies the combination without repetitions and verifies the overlapping of the periods. If overlapped, a counter is increased and printed in the console when the comparison ends.

### Parameters:

#### office_time : dictionary

# Approach and Methodology
For me, the best-used programming language is Python. So, I decided to use the 3.9.2 version in [Pycharm](https://www.jetbrains.com/pycharm/), an IDE designed for Python.  
Input data is presented with patterns in a line-by-line text file. Then, I read each line, split them into different data types, and ordered all data in a dictionary. All this procedure is done in a single function, and another counts the employee coincidences in minutes. The project follows the [Pyton Enhancement Proposals 8 - Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/).

# How to Run
1. Make sure you have installed Python version >= 3.
2. Download `main.py` and optionally `input.txt`. You can  create the input data if you like.
3. Open a shell and navigate to the directory which the program and the input data are located.
4. Execute the program: `python3 main.py` or `python main.py`.
5. See the results.