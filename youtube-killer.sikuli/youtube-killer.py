offset = 270
#Location(505, 407)
#Location(774, 406)
counter = 0
y = 400
def check(r):
    r.click(find("1601722027200.png"))
    if r.exists("1601720279322.png"):
        r.click("1601720279322.png")
        r.highlight()
        if r.exists("1601740984787.png"):
            r.click("1601740984787.png")
            
            if exists("1601741032017.png"):
                click("1601741122980.png")
                click("1601741138519.png")
            elif exists("1601741252942.png"):
                click("1601741273456.png")
                click("1601741138519.png")
                
    elif exists("1601720532100.png"):
        click("1601720532100.png")

for j in range(0, 1000000):
    #if j % 20 == 0:            
    i = 0
    while i < 4:
        region = Region(195 + offset * i, 154, 585 + offset * i, 462)
        #region.highlight()
        mouseMove(Location(505 + offset * i, y))
        if exists("1601722027200.png"):
            check(region)
            i = i + 1
        else: 
            counter = counter + 1
            if counter == 2:
                counter = 0
                click("1601725667791.png")
            elif counter == 2:
                y = 620
                mouseMove(Location(505 + offset * i, y))
                if exists("1601722027200.png"):
                    check(region)
                else:
                    y = 400
            wheel(WHEEL_DOWN, 1)
    wheel(WHEEL_DOWN, 2)