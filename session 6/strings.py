fruit = "banana"
#letter = fruit[2.6]
#print(len(fruit))
#for index in range(len(fruit)):
#    print(f"Letter #{index} is " + fruit[index])
fruit = "mangosteen"
# print("\"" + fruit[:] + "\"")
# print(f'"{fruit[:6]}"')
# print(f"'{fruit[0:6]}'")
#print("male" in fruit)

def compare_to_lemon(fruit):
    if (fruit == "lemon"):
        print("Alright! Lemon pie.")
    elif (fruit < "lemon"):
        print("Boo! Less-than-lemon pie.")
    else:
        print("Sometimes greather-than-lemon pie is ok.")

#fruit = ".emon"
dirty = "hEllo there"
dirty = dirty.replace("there","Potato")
cleaned = dirty.capitalize()
#print(f"'{dirty}' -> '{cleaned}'")

demo = "1,Mabel,Smith,3 Third Ave,Mt Lawley,6666"
spread_out = demo.replace(",","\n")
#print(spread_out)

import math

def get_vertical_force_component(force,angle):
    rads = math.radians(angle)
    return tuple(force, angle, force * math.sin(rads))

print(get_vertical_force_component(54,27))

print(math.asin(0.5) * 180 / math.pi)

