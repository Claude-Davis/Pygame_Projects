RECTS
* Short for "rectangle"
* It is a rectangular area with both (x,y) coordinates and a width and height.
* Create a rect with the constructor below:
    rect = pygame.Rect(x, y, width, height)
-----------------------------------------------------------------------------------------------------------------
WHY USE RECTS?
* Allows you to automatically update surfaces by only change information in the rect.
* Instead of having to calculate coordinates of the bottom right corner of a Rect:
    coordinates = (rect.x + rect.width, rect.y + rect.height)
Helpful Fields:
    - x,y
    - top, left, bottom, right
    - topleft, bottomleft, topright, bottomright
    - midtop, midleft, midbottom, midright
    - center, centerx, centery
    - w,h     
-----------------------------------------------------------------------------------------------------------------
MOVING RECTS
* The move() method updates the position of your Rect.
    rect = rect.move(5,5)
* Be sure to store the move() method since it returns a Rect.
* Moving a rect is really just creating a new rect in  a different location and overwriting the previous rect.
* Include a clock:
    clock = pygame.tick.Clock()
    clock.tick()
-----------------------------------------------------------------------------------------------------------------
STAYING IN-BOUNDS
* The program needs to check if the rect's new position would be off-screen
-----------------------------------------------------------------------------------------------------------------
DIRECTIONS
* Increase x-value = rightward direction
* Decrease x-value = leftward direction
* Increase y-value = downward direction
* Decrease y-value = upward direction
