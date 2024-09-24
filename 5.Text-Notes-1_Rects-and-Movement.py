RECTS
* Short for "rectangle"
* It is a rectangular area with both (x,y) coordinates and a width and height.
* Create a rect with the constructor below:
    rect = pygame.Rect(x, y, width, height)
-----------------------------------------------------------------------------------------------------------------
WHY USE RECTS?
* Allows you to automatically update surfaces by only change information in the rect.
-----------------------------------------------------------------------------------------------------------------
MOVING RECTS
* The move() method updates the position of your Rect.
    rect = rect.move(5,5)
* Be sure to store the move() method since it returns a Rect.
-----------------------------------------------------------------------------------------------------------------
