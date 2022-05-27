import urllib.request
import sys

response = None

fileName = input("Enter the file you would like to read: (include .txt extension \n")
try:
    response = urllib.request.urlopen('https://leff-itcs.s3.amazonaws.com/' + fileName)
except:
    print("File not found")
    sys.exit()

fileData = response.read().splitlines()

sweetPotato = 0
idahoPotato = 0
squash = 0
tomato = 0
greenBeans = 0
totalRevenue = 0

for i in range(len(fileData)):
    fileData[i] = fileData[i].decode('utf-8')
    if "Sweet Potato" in fileData[i]:
        sweetPotato += int(fileData[i + 1])
        totalRevenue += (int(fileData[i + 1]) * 0.5)
    if "Idaho Potato" in fileData[i]:
        idahoPotato += int(fileData[i + 1])
        totalRevenue += (int(fileData[i + 1]) * 0.4)
    if "Squash" in fileData[i]:
        squash += int(fileData[i + 1])
        totalRevenue += (int(fileData[i + 1]) * 0.75)
    if "Tomato" in fileData[i]:
        tomato += int(fileData[i + 1])
        totalRevenue += (int(fileData[i + 1]) * 0.3)
    if "Green Beans" in fileData[i]:
        greenBeans += int(fileData[i + 1])
        totalRevenue += (int(fileData[i + 1]) * 0.45)

print("Total items to be delivered: ")
print("Sweet Potato: " + str(sweetPotato))
print("Idaho Potato: " + str(idahoPotato))
print("Squash: " + str(squash))
print("Tomato: " + str(tomato))
print("Green Beans: " + str(greenBeans))
print("")
print("Total Revenue: " + str(totalRevenue))
