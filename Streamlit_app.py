import streamlit as st

st.title("Tip Calculator")

bill = st.number_input("What was the total bill? $", min_value=0.0, format="%.2f")
tip = st.selectbox("How much tip would you like to give?", [10, 12, 15])
people = st.number_input("How many people to split the bill?", min_value=1, format="%d")

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

st.write(f"Each person should pay: ${final_amount:.2f}")
