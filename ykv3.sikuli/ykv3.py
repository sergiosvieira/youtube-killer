def create_pattern(img, sim=1.):
    pattern = Pattern(img)
    pattern.similar(sim)
    return pattern
normal_preview_pattern = create_pattern("retangulo.png", 0.15)

three_dots_pattern = create_pattern("1601722027200.png")

def click_if_exists(img):
    if exists(img):
        click(img)
        return True
    return False

def wheel_if_exists(img, safe_img, counter = 10):
   if exists(img):
       click(find(safe_img))
       wheel(WHEEL_DOWN, 4)
       return True
   return False

def restart():
    if exists("1601819569379.png"):
        click(find("1601819569379.png"))
        wait(2)

wheel_counter = 0
while True:
    try:
        try:
            all_preview = findAll(normal_preview_pattern)
        except:
            wheel_counter = 0
            restart()
        three_dots_counter = 0        
        for p in all_preview:
            if wheel_counter == 2:
                wheel_counter = 0
                restart()
            mouseMove(p)
            if click_if_exists("1601722027200.png"):
                result = click_if_exists("1601815666312.png")
                if result == False:
                    if wheel_if_exists("1601817295407.png", "1601722027200.png"):
                        wheel_counter += 1
            else:
                three_dots_counter += 1
        if three_dots_counter != 0:
            wheel_counter = 0
            restart()
        wheel(WHEEL_DOWN, 4)
    except Exception as e:
        print(e)
        break;