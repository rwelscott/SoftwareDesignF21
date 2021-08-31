def interface():
    print("Blood Calculator")
    keep_running = True
    while keep_running:
         print("Make a choice")
         print("1- HDL Analysis")
         print("2- LDL Analysis")
         print("3- Total Cholesterol Analysis")
         print("9 - quit")
         choice = int(input("Make a choice: "))
         print(type(choice))
         if choice ==9:
            keep_running = False
         elif choice ==1:
            HDL_Driver()
         elif choice ==2:
             LDL_Driver()
         elif choice ==3:
            Total_Cholesterol_Driver()

        
   
    print(choice)
    return choice

def HDL_Driver():
    HDL_value = hdl_input()
    HDL_character = hdl_analysis(HDL_value)
    hdl_output(HDL_value, HDL_character)

def hdl_input():
    hdl_value = int(input("Enter HDL Value: "))
    return hdl_value
    
def hdl_analysis(HDL_value):
    if HDL_value >=60:
        return "Normal"
    elif 40 <= HDL_value < 60:
        return "Borderline Low"
    else:
        return "Low"

def hdl_output(HDL_value, HDL_answer):
    print("The HDL value of {} is considered {}.".format(HDL_value, HDL_answer))
    



def LDL_Driver():
    LDL_value = ldl_input()
    LDL_character = ldl_analysis(LDL_value)
    ldl_output(LDL_value, LDL_character)

def ldl_input():
    ldl_value = int(input("Enter LDL Value: "))
    return ldl_value
    
def ldl_analysis(LDL_value):
    if LDL_value >=190:
        return "Very High"
    elif 160 <= LDL_value <= 189:
        return "High"
    elif 130 <= LDL_value <= 159:
        return "Borderline High"
    else:
        return "Low"

def ldl_output(LDL_value, LDL_answer):
    print("The LDL value of {} is considered {}.".format(LDL_value, LDL_answer))
    
def Total_Cholesterol_Driver():
    Total_Cholesterol_value = total_chol_input()
    Total_Cholesterol_character = total_chol_analysis(Total_Cholesterol_value)
    total_chol_output(Total_Cholesterol_value, Total_Cholesterol_character)

def total_chol_input():
    total_chol_value = int(input("Enter Total Cholesterol Value: "))
    return total_chol_value
    
def total_chol_analysis(Total_Cholesterol_value):
    if Total_Cholesterol_value <200:
        return "Normal"
    elif 200 <= Total_Cholesterol_value <= 239:
        return "Borderline High"
    elif Total_Cholesterol_value >= 240:
        return "High"


def total_chol_output(Total_Cholesterol_value, Total_Cholesterol_answer):
    print("The Total Cholesterol value of {} is considered {}.".format(Total_Cholesterol_value, Total_Cholesterol_answer))
    
interface()
