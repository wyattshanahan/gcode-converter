def processGcode(fileName, scale, offsetX, offsetY):
    # read data from the gcode file
    content = open(fileName,'r').readlines()
    d,r,i,sp,ep = [],[],0,';LAYER:0',';LAYER:1'
    for line in content:
        i+=1
        if line.find(ep) >= 0:
            e = i
            break
        elif line.find(sp) >= 0:s = i
    for i in range(s+1,e):r.append(content[i].split())
    for i in range(0,len(r)):
        a = r[i]
        if a[0] == 'G1':boolean = True
        elif a[0] == 'G0':boolean = False
        else:continue
        x,y = a[1],a[2]
        if x[0] == 'X':x = a[1]
        elif y[0] == 'X':x,y = a[2],a[3]
        else: continue
        d += [[((float(x[1:]) * scale) + offsetX),((float(y[1:]) * scale) + offsetY),boolean]]
    if len(d) < 15: print(d)
    return d
def gCode(points):
    import turtle
    wn,t = turtle.Screen(),turtle.Turtle()
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
