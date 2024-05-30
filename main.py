import streamlit as st

# Title and description
st.title("Cytokine Release Syndrome (CRS) Grading Calculator")
st.write("""
### Welcome to the CRS Grading Calculator
This application helps healthcare professionals calculate the grade of Cytokine Release Syndrome (CRS) based on patient symptoms. 
Fill in the required information to get the CRS grade.
""")

# User inputs
fever = st.radio("Does the patient have a fever?", ("Yes", "No"))
hypotension = st.radio("Does the patient have hypotension?", ("No", "Not requiring vasopressors", "Requiring one vasopressor", "Requiring multiple vasopressors"))
hypoxia = st.radio("Does the patient have hypoxia?", ("No", "Needing low-flow oxygen", "Needing high-flow oxygen", "Needing positive pressure (CPAP/BiPAP)", "Needing mechanical ventilation"))

# CRS Grading Logic
def calculate_crs_grade(fever, hypotension, hypoxia):
    if fever == "No":
        return "Grade 0: No CRS"
    
    if hypotension == "No" and hypoxia == "No":
        return "Grade 1: Mild CRS"

    if hypotension == "Not requiring vasopressors" and (hypoxia == "No" or hypoxia == "Needing low-flow oxygen"):
        return "Grade 2: Moderate CRS"

    if hypotension == "Requiring one vasopressor" or hypoxia in ["Needing high-flow oxygen", "Needing positive pressure (CPAP/BiPAP)"]:
        return "Grade 3: Severe CRS"

    if hypotension == "Requiring multiple vasopressors" or hypoxia == "Needing mechanical ventilation":
        return "Grade 4: Life-threatening CRS"

    return "Unspecified CRS grade"

# Calculate and display CRS grade
crs_grade = calculate_crs_grade(fever, hypotension, hypoxia)
st.subheader(f"CRS Grade: {crs_grade}")
