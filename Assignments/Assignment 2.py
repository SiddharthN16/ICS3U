#-----------------------------------------------------------------------------
# Name:        Python Assignment 2 (main.py)
# Purpose:     Responsibilities of a Nurse
#
# Author:      Siddharth Nema
# Created:     09-June-2021
# Updated:     15-June-2021
#-----------------------------------------------------------------------------
# Job: Nurse
# Job Description: Provide Medication to Patients & Calculate Cost of Stay
# Three Wings of Hospital to Monitor: Adults, Teens, Children

# Adding logging to program
import logging
logging.basicConfig(filename='log.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

# Available Age Groups
groupsAvail = ["Adult", "Teen", "Child"]

# Lists for Patient's Total Costs
wingOneCost = []
wingTwoCost = []
wingThreeCost = []

def medicine(height, weight, group, avail):
    '''
    Calculates the medicine dose required for a patient

    Receives the height, weight, group, and available groups for patient. If the parameters are valid (correct type & value), proceed with calculation for required medicine dose depending on age group, rounded to two decimal places.

    Parameters
    ----------
    height : int or float
        The height of the patient.
    weight : int or float
        The weight of the patient.
    group : str
        The patient's age group.
    avail : list
        The available age group options.

    Returns
    -------
    float
        The required medicine dose for the patient.

    Raises
    ------
    TypeError
        If the height and weight is not an integer or float, or if the age group is not a string, or if the age groups available is not a list.
    ValueError
        If the height and weight is less than or equal to zero.
    '''
    logging.info(f"medicine() function beginning for {group} patient with height of {height} cm & weight of {weight} kg.")

    # Raises TypeError if one of the parameters is incorrect type
    if not isinstance(height, (int, float)) or not isinstance(weight, (int, float)) or not isinstance(group, str) or not isinstance(avail, list):
        logging.error(f"One of the parameters is an invalid type. ")
        raise TypeError("One of the Parameters is an Invalid Type.")

    # Raises ValueError if any of the values are less than or equal to zero
    if height <= 0 or weight <= 0:
        logging.error(f"Height & weight must be greater than zero.")
        raise ValueError("Height And Weight Must be Greater than Zero.")
    else:
        # Changes the multiplier factor depending on age group
        if group == avail[0]: # Adult
            factor = 100
        elif group == avail[1]: # Teen
            factor = 30
        elif group == avail[2]: # Child
            factor = 10

        # Calculates amount of medicine required and returns the rounded result
        medAmount = (height/weight) * factor
        logging.info(f"The patient would require {medAmount} mg of medicine.")
        return round(medAmount, 2)

def stayCost(dose, citizen):
    '''
    Calculate the Total Stay Cost for the Patient

    Receives the dose and citizen condition for the patient. If the parameters are valid(correct type and value), it proceeds to calculate the per day cost depending on the citizen condition & finds the total cost depending on the medicine dose.

    Parameters
    ----------
    dose : float
        The dose given to patient in milligrams
    citizen : str
        If the patient is a citizen or not

    Returns
    -------
    int
        The final cost for the patient's stay

    Raises
    ------
    TypeError
        If the dose is not a float, or if the citizen variable is not a string
    ValueError
        If the dose is less than or equal to zero.
    '''
    logging.info(f"stayCost() function beginning with a patient requiring {dose} mg of medicine, & citizen state of:{citizen}.")

    # Raises TypeError if one of the parameters is incorrect type
    if not isinstance(dose, float) or not isinstance(citizen, str):
        logging.error(f"One of the parameters is an invalid type.")
        raise TypeError("One of the Parameters is an Invalid Type.")

    # Raises ValueError if dose is less than or equal to zero, or if input for citizen is wrong
    if (dose <= 0) or (citizen != "Y" and citizen != "y" and citizen != "N" and citizen != "n"):
        logging.error(f"One of the parameters has an invalid value.")
        raise ValueError("One of the Parameters has an Invalid Value")
    else:
        # perDay cost changes depending on if patient is citizen or not
        if citizen == "Y" or citizen == "y":
            perDay = 150
        elif citizen == "N" or citizen == "n":
            perDay = 300

        # Calculate days required to stay
        days = round((0.01 * dose) + 1)
        logging.debug(f"{days} days to stay.")

        # Calculate final cost and return value
        totalCost = days * perDay
        logging.info(f"The total cost of stay is ${totalCost}.")
        return totalCost

# medicine() Test Cases
assert medicine(190,85,"Adult",groupsAvail) == 223.53, "An Adult patient who is 190 cm tall & weighs 85 kg, should be given 223.53 mg of medicine."
assert medicine(165,63,"Teen",groupsAvail) == 78.57, "An Teen patient who is 190 cm tall & weighs 63 kg, should be given 78.57 mg of medicine."
assert medicine(90,35,"Child",groupsAvail) == 25.71, "An Child patient who is 90 cm tall & weighs 35 kg, should be given 25.71 mg of medicine."
assert medicine(170,80,"Teen",groupsAvail) == 63.75, "An Teen patient who is 170 cm tall & weighs 80 kg, should be given 63.75 mg of medicine."

# stayCost() Test Cases
assert stayCost(219.19, "N") == 900, "A non-citizen patient taking 219.19 mg of medicine should be charged $900."
assert stayCost(194.84, "Y") == 450, "A citizen patient taking 194.84 mg of medicine should be charged $450."
assert stayCost(51.48, "Y") == 300, "A citizen patient taking 51.48 mg of medicine should be charged $300."
assert stayCost(80.06, "N") == 600, "A non-citizen patient taking 80.06 mg of medicine should be charged $600."

wingOneCount = 0
# Loops until the wing's cost list is the same as the number of patients OR while the list is empty; only allows valid entries
while (len(wingOneCost) != wingOneCount) or (bool(wingOneCost) == False):
    try:
        logging.debug("Gathering information for Wing One.")
        ageGroup = input(f"What is the Age Group for Wing One?: ")

        # Reset values if the program loops again
        wingOneName = []
        wingOneDose = []
        wingOneCost = []
        wingOneCount = 0

        # Loops to ensure acceptable age group is entered & there are no patients currently
        while (ageGroup in groupsAvail) & (wingOneCount == 0):
            wingOneCount = int(input(f"Enter the Number of {ageGroup} Patients: "))

            # Loops to gather information for all patients
            for i in range(wingOneCount):
                wingOneName.append(input(f"\nWhat is Patient #{i+1}'s Name?: "))
                wingOneHeight = float(input(f"Enter {wingOneName[i]}'s Height in Centimetres: "))
                wingOneWeight = float(input(f"Enter {wingOneName[i]}'s Weight in Kilograms: "))
                citizenCheck = input(f"Is {wingOneName[i]} a Citizen? (Y/N): ")

                # Calling the functions to perform calculations
                logging.info(f"Calling medicine() function for adult patient {wingOneName[i]}, who is {wingOneHeight} cm tall & weighs {wingOneWeight} kg.")
                wingOneDose.append(medicine(wingOneHeight, wingOneWeight, ageGroup, groupsAvail))
                logging.info(f"Calling stayCost() function for {wingOneName[i]} who needs {wingOneDose[i]} mg of medicine & citizen state of: {citizenCheck}")
                wingOneCost.append(stayCost(wingOneDose[i], citizenCheck))
        else:
            # Loop again if entered age group is not in list
            if ageGroup not in groupsAvail:
                logging.debug(f"{ageGroup} is not an acceptable age group.")
                print(f"{ageGroup} is not an Acceptable Age Group! Try Again:\n")

    except TypeError as e:
        print(f"A TypeError has Occurred: {e}")
    except ValueError as e:
        print(f"A ValueError has Occurred: {e}")
    else:
        # Print statement for all patients
        for i in range(wingOneCount):
            print(f"{wingOneName[i]} Requires {wingOneDose[i]} Milligrams of Medicine, and Will Cost ${wingOneCost[i]}.\n")
            logging.debug(f"Successfully executed functions, moving onto next wing.")

wingTwoCount = 0
# Loops until the wing's cost list is the same as the number of patients OR while the list is empty
while (len(wingTwoCost) != wingTwoCount) or (bool(wingTwoCost) == False):
    try:
        logging.debug("Gathering information for Wing Two.")
        ageGroup = input(f"What is the Age Group for Wing Two?: ")

        # Reset values if the program loops again
        wingTwoName = []
        wingTwoDose = []
        wingTwoCost = []
        wingTwoCount = 0

        # Loops to ensure acceptable age group is entered & there are no patients currently
        while (ageGroup in groupsAvail) & (wingTwoCount == 0):
            wingTwoCount = int(input(f"Enter the Number of {ageGroup} Patients: "))

            # Loops to gather information for all patients
            for i in range(wingTwoCount):
                wingTwoName.append(input(f"\nWhat is Patient #{i+1}'s Name?: "))
                wingTwoHeight = float(input(f"Enter {wingTwoName[i]}'s Height in Centimetres: "))
                wingTwoWeight = float(input(f"Enter {wingTwoName[i]}'s Weight in Kilograms: "))
                citizenCheck = input(f"Is {wingTwoName[i]} a Citizen? (Y/N): ")

                # Calling the functions to perform calculations
                logging.info(f"Calling medicine() function for adult patient {wingTwoName[i]}, who is {wingTwoHeight} cm tall & weighs {wingTwoWeight} kg.")
                wingTwoDose.append(medicine(wingTwoHeight, wingTwoWeight, ageGroup, groupsAvail))
                logging.info(f"Calling stayCost() function for {wingTwoName[i]} who needs {wingTwoDose[i]} mg of medicine & citizen state of: {citizenCheck}")
                wingTwoCost.append(stayCost(wingTwoDose[i], citizenCheck))

        else:
            # Loop again if entered age group is not in list
            if ageGroup not in groupsAvail:
                logging.debug(f"{ageGroup} is not an acceptable age group.")
                print(f"{ageGroup} is not an Acceptable Age Group. Try Again:\n")

    except TypeError as e:
        print(f"A TypeError has Occurred: {e}")
    except ValueError as e:
        print(f"A ValueError has Occurred: {e}")
    else:
        # Print statement for all patients
        for i in range(wingTwoCount):
            print(f"{wingTwoName[i]} Requires {wingTwoDose[i]} Milligrams of Medicine.\n")
            logging.debug(f"Successfully executed functions, moving onto next wing.")

wingThreeCount = 0
# Loops until the wing's cost list is the same as the number of patients OR while the list is empty
while (len(wingThreeCost) != wingThreeCount) or (bool(wingThreeCost) == False):
    try:
        logging.debug("Gathering information for Wing Three.")
        ageGroup = input(f"What is the Age Group for Wing Three?: ")

        # Reset values if the program loops again
        wingThreeName = []
        wingThreeDose = []
        wingThreeCost = []
        wingThreeCount = 0

        # Loops to ensure acceptable age group is entered & there are no patients currently
        while (ageGroup in groupsAvail) & (wingThreeCount == 0):
            wingThreeCount = int(input(f"Enter the Number of {ageGroup} Patients: "))

            # Loops to gather information for all patients
            for i in range(wingThreeCount):
                wingThreeName.append(input(f"\nWhat is Patient #{i+1}'s Name?: "))
                wingThreeHeight = float(input(f"Enter {wingThreeName[i]}'s Height in Centimetres: "))
                wingThreeWeight = float(input(f"Enter {wingThreeName[i]}'s Weight in Kilograms: "))
                citizenCheck = input(f"Is {wingThreeName[i]} a Citizen? (Y/N): ")

                # Calling the functions to perform calculations
                logging.info(f"Calling medicine() function for adult patient {wingThreeName[i]}, who is {wingThreeHeight} cm tall & weighs {wingThreeWeight} kg.")
                wingThreeDose.append(medicine(wingThreeHeight, wingThreeWeight, ageGroup, groupsAvail))
                logging.info(f"Calling stayCost() function for {wingThreeName[i]} who needs {wingThreeDose[i]} mg of medicine & citizen state of: {citizenCheck}")
                wingThreeCost.append(stayCost(wingThreeDose[i], citizenCheck))
        else:
            # Loop again if entered age group is not in list
            if ageGroup not in groupsAvail:
                logging.debug(f"{ageGroup} is not an acceptable age group.")
                print(f"{ageGroup} is not an Acceptable Age Group. Try Again:\n")

    except TypeError as e:
        print(f"A TypeError has Occurred: {e}")
    except ValueError as e:
        print(f"A ValueError has Occurred: {e}")
    else:
        # Print statement for all patients
        for i in range(wingThreeCount):
            print(f"{wingThreeName[i]} Requires {wingThreeDose[i]} Milligrams of Medicine.\n")
            logging.debug(f"Successfully executed functions, END OF PROGRAM.")
