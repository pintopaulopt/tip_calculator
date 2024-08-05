import streamlit as st

# Title of the app
st.title("Tip Calculator")

# Get the total bill amount from the user
bill = st.number_input("What was the total bill? $", min_value=0.0, format="%.2f")

# Get the tip amount and ensure it is one of the specified values
tip_options = [10, 12, 15]
tip = st.selectbox("How much tip would you like to give?", tip_options)

# Get the number of people to split the bill
people = st.number_input("How many people to split the bill?", min_value=1, format="%d")

# Calculate the tip as a percentage
tip_as_percent = tip / 100

# Calculate the total tip amount
total_tip_amount = bill * tip_as_percent

# Calculate the total bill
total_bill = bill + total_tip_amount

# Calculate the bill per person
bill_per_person = total_bill / people

# Round the final amount to 2 decimal places
final_amount = round(bill_per_person,
