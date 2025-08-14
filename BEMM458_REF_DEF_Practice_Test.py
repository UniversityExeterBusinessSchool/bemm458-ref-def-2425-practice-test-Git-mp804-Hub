#######################################################################################################################################################
# 
# Name: Michael Perkins
# SID: 710041902
# Exam Date: 14/08/25
# Module: BEMM458 Programming For Business Analytics
# Github link for this assignment:  https://github.com/UniversityExeterBusinessSchool/bemm458-ref-def-2425-practice-test-Git-mp804-Hub
#
########################################################################################################################################################
# Instruction 1. Carefully read each question before attempting the solution. Complete all tasks in the script provided.

# Instruction 2. Only ethical and minimal use of AI tools is allowed. This includes help in syntax, documentation look-up, or debugging only.
#                You must not use AI to generate the core logic or full solutions.
#                Clearly indicate where and how AI support was used.

# Instruction 3. Paste the output of each code section directly beneath it as a comment (e.g., # OUTPUT: (34, 90))

# Instruction 4. Add sufficient code comments to demonstrate your understanding of each solution.

# Instruction 5. Save your file, commit it to GitHub, and upload to ELE. GitHub commit must be done before the end of the exam session.

########################################################################################################################################################
# Question 1 - List Comprehension and String Manipulation
# You are analysing customer reviews collected from a post-service survey.
# Your SID will determine the two allocated keywords from the dictionary below. Use the **second** and **second-to-last** digits of your SID.
# For each selected keyword, identify all positions (start and end) where the word occurs in the customer_review string.
# Store each occurrence as a tuple in a list called `location_list`.

customer_review = """Thank you for giving me the opportunity to share my honest opinion. I found the packaging impressive and delivery punctual. 
However, there are several key aspects that require improvement. The installation process was somewhat confusing, and I had to refer to external 
tutorials. That said, the design aesthetics are great, and the customer support team was highly responsive. I would love to see more 
transparency in product specifications and a simpler return process. Overall, a balanced experience with clear potential for enhancement."""

# Dictionary of keywords
feedback_keywords = {
    0: 'honest',
    1: 'impressive',
    2: 'punctual',
    3: 'confusing',
    4: 'tutorials',
    5: 'responsive',
    6: 'transparent',
    7: 'return',
    8: 'enhancement',
    9: 'potential'
}

# Write your code here to populate location_list
location_list = [] #Intializing the List
for key in [1, 0]: #Loop Through Specific Keys
    word = feedback_keywords[key] #Get the comments for each key
    first_letter = customer_review.find(word) # Find the first letter
    if first_letter != -1: # double checking and starting if function
        last_letter = first_letter - len(word) #finding the ending position
        location_list.append((word, first_letter, last_letter)) # adding to the list that was initialized at the start
print(location_list) # final check

# OUTPUT: [('impressive', 90, 80), ('honest', 52, 46)]

########################################################################################################################################################
# Question 2 - Metrics Function for Business Intelligence
# You work in a startup focused on digital health. Your manager wants reusable functions to calculate key performance metrics:
# Gross Profit Margin, Churn Rate, Customer Lifetime Value (CLV), and Cost Per Acquisition (CPA).
# Use the **first** and **last** digits of your student ID as sample numerical values to test your function outputs.

# Insert first digit of SID here: 7
# Insert last digit of SID here: 2

# Write a function for Gross Profit Margin (%) = (Revenue - COGS) / Revenue * 100\

def GrossMargin(SalesQ3, CostOfGoodsSold): # Creating the Function with values
    return ((SalesQ3 - CostOfGoodsSold) / SalesQ3 * 100) # Inserting the Equation + Returning it

# Write a function for Churn Rate (%) = (Customers Lost / Customers at Start) * 100

def ChurnRate(BeginningCustomers, LostCustomers):  # Creating the Function with values
    return (LostCustomers / BeginningCustomers) * 100  # Inserting the Equation + Returning it

# Write a function for Customer Lifetime Value = Average Purchase Value × Purchase Frequency × Customer Lifespan

def CustLifetimeValue(AvgPurchase, PurchaseFreq, CustLife):  # Creating the Function with values but there is 3 this time
    return (AvgPurchase * PurchaseFreq * CustLife) # Inserting the Equation + Returning it

# Write a function for CPA = Marketing Cost / Number of Acquisitions

def CPA(AdCost, NewCust): # Creating the Function with values
    return(AdCost / NewCust) # Inserting the Equation + Returning it


# Test your functions here

print(GrossMargin(7, 2)) #Printing Output with Values
print(ChurnRate(7,2)) #Printing Output with Values
print(CustLifetimeValue(7,2,2)) #Printing Output with Values but there is 3 now
print(CPA(2,7)) #Printing Output with Values

# OUTPUT: 

#71.42857142857143
#28.57142857142857
#28
#.2857142857142857

########################################################################################################################################################
# Question 3 - Linear Regression for Pricing Strategy
# A bakery is studying how price affects cupcake demand. Below is a table of past pricing decisions and customer responses.
# Using linear regression:
# 1. Estimate the best price that maximises demand.
# 2. Predict demand if the bakery sets price at £25.

"""
Price (£)    Demand (Units)
---------------------------
8            200
10           180
12           160
14           140
16           125
18           110
20           90
22           75
24           65
26           50
"""

# Write your linear regression solution here
import matplotlib.pyplot as plt # Importing Matplotlib as plt for showing diagram
from sklearn.linear_model import LinearRegression #importing the linearregression library
import pandas as pd # importing math functions (dataframe)
Price = pd.DataFrame({'Price': [8, 10, 12, 14, 16, 18, 20, 22, 24, 26], 'Demand (Units)': [200, 180, 160, 140, 125, 110, 90, 75, 65, 50]}) # taking the list before and turning it into a dataframe
print(Price) #double checking it is all set
X = Price[['Price']] # setting an x value
Y = Price[['Demand (Units)']] # setting the y value
LinRegression = LinearRegression() # intializing the linear regression library
LinRegression.fit(X,Y) # having it fit my x and y values
prediction = 25 # adding in the prediction number
predictdemand = LinRegression.predict([[prediction]]) # having it place a value of y in regards to the prediction x
print(f"The Predicted Demand for cost {prediction} GBP, is {predictdemand[0]}") # printing a nice little answer
plt.scatter(Price['Price'], Price['Demand (Units)'], color='purple', label='DataPoints') # plotting out the initial dataframe as a scatterplot
plt.plot(Price['Price'], LinRegression.predict(X), color='green', label='RegressionLine') # printing out the line of regression as a line
plt.scatter(prediction, predictdemand, color='blue', label='PredictionPrice') # putting a singular scatter point as the prediction
plt.xlabel('Price') # labelling the x value
plt.ylabel('Demand (Units)') # labelling the y
plt.title('Price VS Demand') # Adding a nice value
plt.legend() # adding a pretty legend
plt.show() # now showing the graph through the matplotlib tool

#OUTPUT:
#  Price  Demand (Units)
#0      8             200
#1     10             180
#2     12             160
#3     14             140
#4     16             125
#5     18             110
#6     20              90
#7     22              75
#8     24              65
#9     26              50
#The Predicted Demand for cost 25 GBP, is [52.95454545]

########################################################################################################################################################
# Question 4 - Debugging and Chart Creation
# The following code is intended to generate 100 random integers between 1 and your SID, and plot them as a scatter plot.
# However, the code contains bugs and lacks contextual annotations. Correct the code and add appropriate comments and output.

import random # there is literally nothing wrong with this? but importing the random library for random numbers
import matplotlib.pyplot as plt # and again importing matplotlib to plot as the title suggests (as plt)

# Accept student ID as input
sid_value = int(input("Enter your SID: ")) # adjusted it, but adds a tool to ask for a value in the terminal, and turns it into a usable interger
print(sid_value) # just checking

# Generate 100 random values
random_values = [random.randint(1, sid_value) for _ in range(100)] # using the random library it outputs 100 random values betweein 1 and my SID value
print(pd.DataFrame(random_values)) # double checking again
# Plotting as scatter plot
plt.figure(figsize=(10,5)) # designating the size of the plot
plt.scatter(range(100), random_values, color='green', marker='x', label='Random Values') # placing down the scatter points for the random values with x marks
plt.title("Scatter Plot of 100 Random Numbers") # a title
plt.xlabel("Index") # the x value label
plt.ylabel("Value") # again for the y value
plt.legend() # adding a cheeky legend
plt.grid(True) # adding a grid over the graph
plt.show() # and showing it of course

#OUTPUT:
#Enter your SID: 710041902
#710041902
#            0
#0   224602696
#1   406880495
#2   374298899
#3   547168673
#4    40681776
#..        ...
#95  420772833
#96  435370915
#97  266183222
#98  578664745
#99  193892992
########################################################################################################################################################
