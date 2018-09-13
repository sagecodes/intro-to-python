# Learn to Code: Introduction to Python

Brought to you by Galvanize. Learn more about the way we teach at [galvanize.com](http://galvanize.com).

Get to this repo by typing in URL: **py.sage.codes**

## Overview
The goal of this brief course is to provide you with a fun introduction to the world of development with Python.

#### Here's what we'll be doing:
* Overview of basic Python and programming concepts
* Building a simple application using Python
* Playing around and break things


#### What is programming?
Programming is giving your computer a set of instructions to perform a task. 

This sounds simple but it can get complicated! 


## Setting up your computer


#### Please set up the following:

* A web browser to see what we're working on as others see it (Recommend Google Chrome: [chrome.google.com] (http://chrome.google.com))
* We will be using an online text editor for this workshop. You can sign up here: [https://repl.it/](https://repl.it/)


Well... that was easy! 


## What this workshop is

A super friendly introduction to Python No previous experience expected! 

You can't learn EVERYTHING in ~2 hours. But you can learn enough to get excited and comfortable to keep working and learning on your own! Come to our almost weekly code hours [meetups](https://www.meetup.com/Learn-Code-Seattle/events/) to ask questions if you get stuck and show off what you've been working on!

- This course is for absolute beginners
- Ask Questions!
- Answer Questions!
- Help others when you can
- Its ok to get stuck, just ask for help!
- Feel free to move ahead
- Be patient and nice


## About me:
Hello I'm [Sage Elliott](http://sageelliott.com/). I'm a Technology Evangelist here at Galvanize! Previously I've worked as a software and hardware engineer with Startups and Agencies in Seattle, WA and Melbourne, FL. I love technology! I'm currently learning more about building AI and VR projects. 

- Website: [sageelliott.com](http://sageelliott.com/)
- Twitter: [@sagecodes](https://twitter.com/@sagecodes)
- LinkedIn: [sageelliott](https://www.linkedin.com/in/sageelliott/) 
- Email: [sage.elliott@galvanize.com](mailto:sage.elliott@galvanize.com)


## About you!

Give a quick Intro!

- Whats your name?
- Whats your background?
- Why are you interested in JavaScript?

## What is Python?

### A very brief history

Created by Guido van Rossum and released in 1991.

Python is Known ease of learning, code readability (must use code indents), and a massive ecosystem of libraries that easily expand its usefeullness is many fields.

Read more about the history of Python [here](https://en.wikipedia.org/wiki/Python_(programming_language)).


### Who uses Python?

A lot of places do!

- Large Companies (Google, Facebook)
- Startups
- Agencies
- Majority of companies doing data science 

### What can you do with Python

- Web Development
	- Back-End (frameworks: Django, Flask, more)
- Mobile Development 
- Data Science and AI
	- Data Analysis
	- Machine Learning
	- Deep Learning
	- Computer Vision
	- Natural Language Processing
- [Embedded(Hardware)](https://micropython.org/)
- Devops

#### Popular Frameworks and libraries to keep in mind

When learning more about Python you'll probably see someo of these pop up as you continue to study

- Web
	- Django
	- Flask
	- pyramid


- Data Science
	- Tensorflow
	- Keras
	- Numpy
	- Pandas 

*Note*: if you're thinking of exploring data science with python look into using [Anaconda](https://www.anaconda.com/) to manage your python and data libraries


## Python Basics:

### Data Types:
We're going to stick with the basics, so We wont be going over EVERY data type in Python, but you you can read a more comprehensive list [here](https://docs.python.org/3/library/stdtypes.html#dict).  

Feel free to try these different data types out in your code!

#### Numbers:

Numbers are written just like you would think. Just the number! No quotes or symbols to worry about. If you do put quotes around a number it will become a string (see next)

`25` `100`

Multiple, Add, Divide, Compare

- `5 * 5` | output: 25
- `5 + 5` | output: 10
- `8 / 2` | output: 4
- `8 > 2` | output: true

#### Strings:
Strings can be a collection of letters, symbols and/or numbers. They are made by surrounding the content with quotation marks.

`"Hello, World."`
`"CrAzy Random String 987879896jvdjvda &&(&(@*(*"`

can use double: ", Single ' or tripple(3 singles) ''' quotes for strings.

Can we add strings together? Try it out!


#### Booleans:
You can think of Booleans as yes(true) and no(false)

`True` `False`

We'll go into how to use these in a little bit. For now just remember they exist!


#### Lists (Arrays)

Often used to store a list of values.

```
tvshows = ['West World','Mr. Robot', 'Game of Thrones']
print(tvshows)
```

read more about python lists[here](https://www.w3schools.com/python/python_lists.asp).


#### Dictionary (Dict)

Dictionaries can also be used to store values, but they are indexed. 

person =	{
  "name": "Bob",
  "age": 50,
  "occupation": 'programmer'
}
print(person)
print(person['name'])

read more about python dictionaries[here](https://www.w3schools.com/python/python_dictionaries.asp).


## Variables:
Variable are a way to store information.
This is super useful! You can then receive or update the variable in your program. You'll see this later!

Think of it as naming a piece of data.

its common in programming languages to have a keyword before the variable such as `var` or `int`, but python does not need this. 

- `twitter = "@sagecodes";`
- `score = 0;`


## Comparison Operators:
Comparison Operators are used quite frequently in programming. Its a great way to compare and use data.

Again we won't cover ALL of the comparison operators in this workshop, but you can see a full list of them [here](https://docs.python.org/3/library/stdtypes.html#comparisons)

- `==` Equal
- `!=` Not Equal
- `>` Greater Than
- `>=` Greater Than or Equal
- `<` Less Than
- `<=` Less Than or Equal

Example:

`current_score >= highest_score`
This would return a boolean value. Depending on the values of these variables this would return either `True` or `False`. Try it in your console using numbers instead of variables!


## Functions
Reduce, Reuse, Recycle

Functions make it easy to reuse code. If you find yourself repeating code you may want to turn it into a function!

Example:
This function takes in two arguments(a, b) and returns the value of them added together. 

```
def add(a, b):
	print(a + b)
```
to use the function call it by writing its name and open/close parenthesis(). With arguments passed inside the parenthesis():

- `add(5,5)` | output: 10
- `add(2,5)` | output: 7

In this simple example you're not saving a ton of code, but imagine a function that uses many lines of code! 


## Conditionals

When writing a program you'll often want to check if data meets a certain condition or not. We can use conditionals to make decision about our data and create different outcomes

 In javascript you'll often use the `if` statement. This may be followed by `else if` or `else` depending on how many conditions need to be checked.

Example:

```
 if guess == answer:
      message = "You Win!"
  elif guess < answer:
      message = "Your guess is too low!"
  elif guess > answer:
      message = "your guess is too high!";
  else:
    message = "I think you entered something wrong..."

```

## Loops
We're going to go over some of the basic loops in javascript, but yet again we're not going to cover everything, so you may want to read more about loops [here](https://www.learnpython.org/en/Loops).

Loops are used when you want to repeat something. You can repeat the exact same thing, or change some variable and repeat the action again.

two common types of loops are `for` and `while`.
`for` loops are often used to run a loop a specified amount of time.

`while` loops are often used to run a loop indefinitely until certain criteria are met.

Example:

This `for` loop will run 5 times, and print out the value of `x` to the console. 

for loop:

```
for x in range(5):
    print(x)
```

For loops are often used to loop through variables containing lists and dicts to get the individual values stored in them. 

Try running these:
```
arr = [1,"hi",6,6]
for x in arr:
    print(x)
```    
```    
word = "Hello"
arr = [1,"hi",6,6]
for x in word:
    print(x)
```

```
info = {'name': 'sage', 
        'language':"python" }
for x in info:
    print(info[x])
```

read more on for loops [here](https://www.w3schools.com/python/python_for_loops.asp)



while loop:

```
count = 1
while count <= 5:
    print(count)
    count += 1  # This is the same as count = count + 1
```


read more on while loops [here](https://www.w3schools.com/python/python_while_loops.asp)

## Interact with users

Getting input from the command line can be useful.

To do that we will use the `input` function. And we want to assign that input to a variable.

`guess = input("enter guess")`


## Lets do some code!
You just learned a lot! Lets put it together and build something!

Sign up if you haven't already and create a new project: https://repl.it/


We're going to build a number guessing game using:

- variables
- Comparison Operators
- Conditionals
- loops
- functions
- dialog boxes

If you get stuck or want to look ahead at the completed project you can view it [here](https://repl.it/@SageElliott/GuessingGame).

What are some ideas for improvements? 

- Exit on command
- data validation
- input the number range from popup
- output grammar depending on number of tries


# YOU DID IT! YOU'RE NOW A PROGRAMMER!

### Welcome! :)

### Keep learning!

[PuPPy](https://www.meetup.com/PSPPython/) is an awesome python group in Seattle! 

More learning resources:

- [w3schools](https://www.w3schools.com/python/default.asp) | Free
- [Datacamp](https://www.datacamp.com/courses/intro-to-python-for-data-science) | Free
- [codecademy: learn-python](https://www.codecademy.com/learn/learn-python) | Free
- [Treehouse: Learn Python Track](https://teamtreehouse.com/tracks/learn-python) | Paid
- [Udacity Programming Foundations with Python](https://www.udacity.com/course/programming-foundations-with-python--ud036) | Free

## What is Galvanize?
###### We are a community!


## Upcoming Events
 
We host sooo many events! check out out [calendar](https://www.galvanize.com/seattle/events)

- [Learn to Code Workshop: Intro to Git and GitHub](https://www.meetup.com/Learn-Code-Seattle/events/253466429/) - Wednesday, September 19, 2018 6:30 PM to 8:30 PM
- [Code Hours](https://www.meetup.com/Learn-Code-Seattle/events/mnlqdqyxmbhc/) - Tuesday, September 25, 2018 6:30 PM to 8:30 PM
- [Learn to Code Workshop: Intro to HTML & CSS](https://www.meetup.com/Learn-Code-Seattle/events/253466466/) - Thursday, September 27, 2018 6:30 PM to 8:30 PM

I post a weekly list of meetups I think I awesome in Seattle [here](http://sageelliott.com/meetups/).


#### Immersive Bootcamp
- [Data Science](https://www.galvanize.com/seattle/data-science) - 9/17/2018
- [Web Development](https://www.galvanize.com/seattle/web-development) - 9/10/2018

#### Part-Time Courses
- [Data Analytics](https://www.galvanize.com/seattle/data-analytics) - 9/24/2018
- [Web Development Foundations with JavaScript](https://www.galvanize.com/seattle/web-development-foundations) - 10/8/2018
- [Data Science Fundamentals](https://www.galvanize.com/seattle/data-science-fundamentals) 9/10/2018



#### Co-working Space
[work in our building!](https://www.galvanize.com/entrepreneur)



## Questions:
Please feel free to reach out to me with any questions!

- Twitter: [@sagecodes](https://twitter.com/@sagecodes)
- LinkedIn: [sageelliott](https://www.linkedin.com/in/sageelliott/) 
- Email: [sage.elliott@galvanize.com](mailto:sage.elliott@galvanize.com)

#### About the Instructors

[Sage Elliott](https://www.linkedin.com/in/sageelliott/) is a technology evangelist for Galvanize based in Seattle. Previously he worked as a Software and hardware engineer for startup around Seattle WA and Melbourne Fl.

You can email him at [sage.elliott@galvanize.com](mailto:age.elliott@galvanize.com) or tweet [@sagecodes](https://twitter.com/sagecodes) for any further questions.





