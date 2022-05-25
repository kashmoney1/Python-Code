import matplotlib.pyplot as plt

xCoords = []
yCoords = []
lineNum = 0
v = input("Enter Velocity: ")
a = input("Enter Launch Angle: ")

file = open("C:/Users/881057/Code/ITCS-Unit-3/AngryRobotsData/RobotData" + v + "v" + a + "d.txt", "r")

coords = file.readlines()
for i in coords:
    if lineNum % 3 == 0:
        xCoords.append(i)
    elif (lineNum - 1) % 3 == 0:
        yCoords.append(i)
    lineNum += 1

for i in range(len(xCoords)):
    xCoords[i] = xCoords[i].strip()
    xCoords[i] = float(xCoords[i])

for i in range(len(yCoords)):
    yCoords[i] = yCoords[i].strip()
    yCoords[i] = float(yCoords[i])

plt.plot(xCoords, yCoords, 'r')
plt.xlabel("Displacement")
plt.ylabel("Height")
plt.title("Height vs. Displacement (V: " + v + " D: " + a + ")")
plt.show()
