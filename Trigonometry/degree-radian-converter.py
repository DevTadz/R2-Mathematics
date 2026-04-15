from enum import Enum
import math
import re

class Command(Enum):
    DegreeToRadian = 1
    RadianToDegree = 2
    Quit = 3

class Radian():
    def __init__(self, pi_coefficient, pi, denominator):
        self.pi_coefficient = pi_coefficient 
        self.pi = pi
        self.denominator = denominator

pi_decimal = 3.14
pi_str = "π"

def main():
    gameRunning = True
    while(gameRunning):
        try:
            print("1: Degree -> Radian")
            print("2: Radian -> Degree")
            print("3: Quit")

            choice = input("Define command: ")

            if(int(choice) is not Command.DegreeToRadian.value and int(choice) is not Command.RadianToDegree.value and int(choice) is not Command.Quit.value):
                raise ValueError("Command doesnt exist!")

            if(int(choice) == Command.DegreeToRadian.value):
                DegreeToRadian()
            elif(int(choice) == Command.RadianToDegree.value):
                RadianToDegree()
            elif(int(choice) == Command.Quit.value):
                print("Goodbye!")
                gameRunning = False

            print("_______________________________")
            print("")
        except ValueError as e:
            print(f"Error: {e}")

def DegreeToRadian():
    degree = input("Degree: ")
    degreeAsInt = int(degree)

    commonFactor = math.gcd(degreeAsInt, 180)
    denominator = math.floor(180/commonFactor)

    radian = f"{math.floor(degreeAsInt/commonFactor)}{pi_str}"

    if(denominator > 1):
        radian += f"/{denominator}"

    print(f"Radian: {radian}")


def RadianToDegree():
    print("Expected input example: 3pi/6")
    radianStr = input("Radian (write π as 'pi'): ")
    radian = Radian("", "pi", "")

    piWithCoefficientAndDenominator = re.search("^\d+pi\/\d+$", radianStr)
    piWithCoeffictient = re.search("^\d*pi$", radianStr)

    if(piWithCoefficientAndDenominator):
        arr = radianStr.split("pi")

        if(arr[0] != " "):
            radian.pi_coefficient = arr[0]
        
        if(arr[1] != " "):
            radian.denominator = arr[1].replace("/", "")

        degree = (int(radian.pi_coefficient)* 180) / int(radian.denominator)
    elif(piWithCoeffictient and radianStr != "pi"):
        arr = radianStr.split("pi")

        if(arr[0] != " "):
            radian.pi_coefficient = arr[0]

        degree = int(radian.pi_coefficient) * 180
    elif(radianStr == "pi"):
        degree = 180

    print(f"{radianStr} = {math.floor(degree)}°")

main()
