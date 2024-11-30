
# # print("Starting new Python")
# import pyjokes
# print("Printing Jokes...")
# joke = pyjokes.get_joke()
# print(joke)
# # #Read,Evaluate,Print,Loop
# # """Docstring is printing"""
# import pyttsx3
# engine = pyttsx3.init()
# engine.say("starting the new course of Python. This is mainly designed for the students to learn the basic syntax of the python and use it in the learning of Artificial Intelligence and Machnie Learning.")
# engine.runAndWait()
#pip install numpy
#TO GET THE DATASET FROM THE SKLEARN LIBRARY
#GENERIC LIBRARIES

# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np


from sklearn.datasets import fetch_california_housing
# GET THE DATA SET
data = fetch_california_housing()