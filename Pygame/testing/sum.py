# import pygame module in this program
import pygame

# activate the pygame library .   
# initiate pygame and give permission   
# to use pygame's functionality.   
pygame.init()

# create the display surface object   
# of specific dimension..e(500, 500).   
win = pygame.display.set_mode((500, 500))

# set the pygame window name  
pygame.display.set_caption("Moving rectangle")

# marker current co-ordinates  
x = 200
y = 200

# dimensions of the marker 
width = 15
height = 15
rect_surface = pygame.Surface((width,height), pygame.SRCALPHA)
rect_surface.fill((255, 0, 0, 128))
# velocity / speed of movement 
vel = 10
color = (255,0,0)
# Indicates pygame is running 
run = True

# infinite loop  
while run:
    # creates time delay of 10ms  
    pygame.time.delay(20)

    # iterate over the list of Event objects   
    # that was returned by pygame.event.get() method.   
    for event in pygame.event.get():

        # if event object type is QUIT   
        # then quitting the pygame   
        # and program both.   
        if event.type == pygame.QUIT:
            # it will make exit the while loop
            run = False
    # stores keys pressed  
    keys = pygame.key.get_pressed()
    win.fill((0,0,0))
    win.blit(rect_surface, (x, y))
    
    # if left arrow key is pressed 
    if keys[pygame.K_LEFT] and x > 0:
        # decrement in x co-ordinate
        x -= vel

        # if left arrow key is pressed
    if keys[pygame.K_RIGHT] and x < 500 - width:
        # increment in x co-ordinate
        x += vel

        # if left arrow key is pressed
    if keys[pygame.K_UP] and y > 0:
        # decrement in y co-ordinate
        y -= vel

        # if left arrow key is pressed
    if keys[pygame.K_DOWN] and y < 500 - height:
        # increment in y co-ordinate 
        y += vel


    # drawing spot on screen which is rectangle here  
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))

    # it refreshes the window 
    pygame.display.update()

# closes the pygame window  
pygame.quit()