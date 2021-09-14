
def data_input():
    x1=int(input("Enter x1: "))
    y1=int(input("Enter y1: "))
    point1=(x1,y1)
    x2=int(input("Enter x2: "))
    y2=int(input("Enter y2: "))
    point2=(x2,y2)
    x_parameter= int(input("Enter a x coordinate: "))
    intpoints = [point1, point2]
    return intpoints, x_parameter
    
def slope_calc(intpoints):
    slope = (intpoints[1][1]-intpoints[0][1])/(intpoints[1][0]-intpoints[0][0])
    return slope

def y_para_calc(intpoints, slope, x_parameter):
    y_parameter=(slope*(x_parameter-intpoints[0][0]))+intpoints[0][1]
    print("The corresponding y value to the x value of {} on this line is {}.".format(x_parameter,y_parameter))
    return y_parameter

def line_driver():
    intpoints, x_parameter= data_input()
    slope = slope_calc(intpoints)
    y_parameter = y_para_calc(intpoints, slope, x_parameter)


if __name__ == "__main__":
    line_driver()
