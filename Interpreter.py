from typing import Match

# strip and head system
inputIndex = 0                                                      # txt file index
tempIndexCounter = 0                                                # txt temp index counter during loop
strip = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]     # list of 27 int
headIndex = 0                                                       # start with head at index 0
startLoopHeadIndex = 0                                              # the index to check to end the loop
loopStartIndex = 0                                                  # start strip index during loop
consoleOutput = []                                                  # the output to print on console

# functions
def PrintHeader():
    i = 0
    while i < 180:
        print("*", end = "")
        i += 1
    print("\n")

def PrintFooter():
    i = 0
    print("\n")
    while i < 180:
        print("*", end = "")
        i += 1
    
def txtFileIndexIncrement():
    global inputIndex
    inputIndex += 1

def MoveForward():      # Move forward the head if not at the end of the strip
    global headIndex
    if headIndex < 26:
        headIndex += 1
    txtFileIndexIncrement()
    IncrementTempIndexCounter()

def MoveBackward():     # Move backward the head if not at the begin of the strip
    global headIndex
    if headIndex > 0:
        headIndex -= 1
    txtFileIndexIncrement()
    IncrementTempIndexCounter()

def IncrementValue(_strip):     # Increment value at specific strip index
    _strip[headIndex] += 1
    txtFileIndexIncrement()
    IncrementTempIndexCounter()

def DecrementValue(_strip):     # Decrement value at specific strip index
    _strip[headIndex] -= 1
    txtFileIndexIncrement()
    IncrementTempIndexCounter()

def AddToOutputList(_strip):    # Convert value and put it in the outpute list as string
    global consoleOutput
    consoleOutput.append(chr(_strip[headIndex]))
    txtFileIndexIncrement()
    IncrementTempIndexCounter()

def PrintOutput():
    print("STRIP: ", end = " ")
    print(strip)
    print("OUTPUT:", end =" ")
    print(*consoleOutput)

def StartLoop(_strip):
    global startLoopHeadIndex
    startLoopHeadIndex = headIndex
    SetLoopStartIndex()
    txtFileIndexIncrement()
    global tempIndexCounter
    tempIndexCounter += 1

def EndLoop(_strip):
    if _strip[startLoopHeadIndex] > 0:
        global tempIndexCounter
        global inputIndex
        inputIndex -= tempIndexCounter
        tempIndexCounter = 0
    else:
        txtFileIndexIncrement()

def IncrementTempIndexCounter():
    global tempIndexCounter
    if tempIndexCounter > 0:
        tempIndexCounter += 1

def SetLoopStartIndex():
    global loopStartIndex
    if loopStartIndex == 0:
        loopStartIndex = inputIndex
    else:
        loopStartIndex += 1

def TakeUserInput():
    userInput = input("Waiting for input: ")
    strip[headIndex] = ord(userInput)
    txtFileIndexIncrement()

def ReadImputFile(fileToRead):
    with open(fileToRead) as file:
        while 1:
            file.seek(inputIndex)
            letter = file.read(1).strip()          # read one char at time and remove the last new line char
            if not letter:                         # stop loop at the end of the file
                break
            match letter:                          # match the content of the file
                case ">":
                    MoveForward()
                case "<":
                    MoveBackward()
                case "+":
                    IncrementValue(strip)
                case "-":
                    DecrementValue(strip)
                case ".":
                    AddToOutputList(strip)
                case "[":
                    StartLoop(strip)
                case "]":
                    EndLoop(strip)
                case ",":
                    TakeUserInput()

# execution
PrintHeader()
ReadImputFile("User_Input.txt")
PrintOutput()
PrintFooter()