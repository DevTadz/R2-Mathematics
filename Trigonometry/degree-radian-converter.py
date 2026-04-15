# Write a function that converts angles from degrees to radians and vice versa, keeping in 
# mind that most programming math libraries (like JavaScript's Math) use radians.
from enum import Enum
import math

class Command(Enum):
    DegreeToRadian = 1
    RadianToDegree = 2

pi_decimal = 3.14
pi_str = "π"

def main():
    print("1: Degree -> Radian")
    print("2: Radian -> Degree")

    choice = input("Define command: ")

    if(int(choice) == Command.DegreeToRadian.value):
        DegreeToRadian()
    elif(int(choice) == Command.RadianToDegree.value):
        RadianToDegree()
    else:
        print("Error")

def DegreeToRadian():
    degree = input("Degree: ")
    degreeAsInt = int(degree)

    commonFactor = math.gcd(degreeAsInt, 180)
    denominator = math.floor(180/commonFactor)

    radian = f"{math.floor(degreeAsInt/commonFactor)}{pi_str}"

    if(denominator > 1):
        radian += str(denominator)

    print(f"Radian: {radian}")


def RadianToDegree():
    radian = input("Radian: ")

main()
