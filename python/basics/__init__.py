import math
def convert_pressure(kpa):
    sum=0
    for i in str(kpa):
        sum+=int(i)
    return sum

print(convert_pressure(1234))