def processGcode(fileName, scale, offsetX, offsetY):
    # read data from the gcode file
    content = open(fileName,'r').readlines()
    i = 0 #initialise the iterator
    d,r = [],[]
    startingPoint = ';LAYER:0' # find the starting point (layer 0)
    endPoint = ';LAYER:1' # find the end point, where the next layer would start in 3D space
    for line in content:
        i+=1 # increment to reach each line
        if line.find(endPoint) >= 0: # if reached the end of the Layer 0, then break
            lnCount = i # set the count for the number of lines in layer 0 to i
            break # break for loop
        elif line.find(startingPoint) >= 0:s = i # if on layer 0 with no value, then this must be the starting point
    for i in range(s+1,lnCount):r.append(content[i].split())
    for i in range(0,len(r)): # iterate through the list
        currData = r[i] # pull in the current list of data (G0, x, y)
        if currData[0] == 'G1': extrude = True # if the value is G1, then move and output pixels
        elif currData[0] == 'G0': extrude = False # if the value is G0, then move but don't output picels
        else: continue # if there's no data, then continue
        x,y = currData[1],currData[2] # set the x and y coordinates from the current data set
        if x[0] == 'X':x = currData[1]
        elif y[0] == 'X':x,y = currData[2],currData[3]
        else: continue
        d += [[((float(x[1:]) * scale) + offsetX),((float(y[1:]) * scale) + offsetY),extrude]]
    if len(d) < 15: print(d)
    return d
def gCode(points):
    import turtle
    wn,t = turtle.Screen(),turtle.Turtle() # initialise the turtle and turtle graphics
    wn.tracer(0)
    for x, y, extrude in points:
        if extrude:t.down()
        else:t.up()
        t.goto(x, y)
    wn.exitonclick()
if __name__ == "__main__":
    # takes input from the user for a few different parts of the process
    fileName = input("Enter the file name: ")
    scale = int(input("Enter the scale:"))
    offsetX, offsetY = int(input("Enter the X offset: ")), int(input("Enter the Y offset: "))
    points = processGcode(fileName, scale, offsetX, offsetY) # processes the gcode using the input from the user
    gCode(points)     # calls the function to draw using turtle graphics
