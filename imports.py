"""
Use compounding interest rates and initial investment to find your return on investment
and calculate the taxes owed
"""

# INSERT IMPORT STATEMENT HERE # FIXME
interest import annual_interest
# TODO: Section 1
# Create a file called "interest.py". Copy/paste the contents from "interest.py" in
# the lesson folder on Github into your own file.

# Import the annual_interest and TAX_RATE constants from the file "interest.py" in this file.

# Ask a user how much they would like to invest with an input statement. Set it equal to a variable
# named "investment".
# TIP: Don't forget to convert the input to an integer!

# Calculate how much their investment would appreciate in one year by multiplying
# the investment variable by the annual_interest. Set the new amount
# equal to a variable named "appreciation".
investment = int(input("How much they would like to invest?: "))
appreciation = investment * annual_interest
print(f"Testing- appreciation: {appreciation}")
annual_interest = .0725
TAX_RATE = .20





# TODO: Section 1.1

# Create a new variable named "new_value" by adding the "appreciation" variable to the
# "investment" variable.
new_value = investment + appreciation 


# Calculate the taxes you have to pay by setting a variable of "taxes" equal to
# the "appreciation" variable times the TAX_RATE.
txes = appreciation * TAX_RATE 

# Print to the user the following output using f shorthand: "Your investment of ${investment} is now worth
# ${new_value} and you owe ${taxes} in taxes." Format the dollar amounts to have two decimal points.
print(f"the investment of ${investment} is now worth ${new_value} and you owe ${taxes} in taxes.")
