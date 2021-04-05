import sys

# Helper functions 
# ====================================================================
def myFunction(x):
    return (2*x + 1)

def deltaX(a,b,interval):
    result = (b - a)/interval 
    return result

def getUpperLower():
    upper = 0
    lower = 0
    while True:
        try:
            upper = int(input("Upper Limit ? > "))
            lower = int(input("Lower Limit ? > "))
            break
        except ValueError:
            print("Enter Int only")
    return upper,lower
def findPoints(pointsList,xo,delX):
    points = []
    # xi = xo + i*delX 
    for x in pointsList:
        xi = int(xo) + x*delX 
        xi = round(xi,2)
        point = (x,xi)
        points.append(point)
    return points

def areaOfRectangle(fxi,delX):
    # receives fxi and delX and returns area of rect
    area = 0
    area = fxi * delX
    return area

def sumOfRectangles(points,delX):
    sumOfRects = 0
    for x in points:
        fxi = myFunction(x[1])
        print(f"{x[0]} : f({x[0]}) = {fxi}")
        area = areaOfRectangle(fxi,delX)
        print(area)
        sumOfRects = sumOfRects + area
        sumOfRects = round(sumOfRects,2)
    return sumOfRects
    
# =======================================================
# Main Function
# =======================================================

def main():
    interval = 0
    interval = int(input("Intervals ? > "))
    upper = 0
    lower = 0
    delX = float(0)
    # Set upper and lower

    upper , lower = getUpperLower()
    # Find delx
    delX = deltaX(lower,upper,interval)
    # find points value x1,x2 .... xn
    pointsList = [x for x in range(1,interval+1)]
    points = list()
    # This returns value like, [(x1,x1.value),(x2,x2.value),.....]
    points = list(findPoints(list(pointsList),lower,delX))
    print(points)
    overAllSum = 0
    overAllSum = sumOfRectangles(points,delX)

main()
