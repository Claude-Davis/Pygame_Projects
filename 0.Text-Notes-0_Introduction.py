INSTALLATION
* https://www.pygame.org/
-----------------------------------------------------------------------------------------------------------------
STARTING A NEW PROJECT
  import pygame
-----------------------------------------------------------------------------------------------------------------
EXAMPLE GAMES
* Aliens
    import pygame
    import pygame.examples.aliens as al
    al.main()
* Monkey Fever
    import pygame
    import pygame.example.chimp as chimp
    chimp.main()
* Cursor          # interactive and color changing aspects
    import pygame
    import pygame.examples.cursors as cur
    cur.main()
* Piano          # music and interactive aspects
    import pygame
    import pygame.examples.midi as mid
    mid.main()
* Playmus
    import pygame
    import pygame.examples.playmus as pm
    pm.main("hymn-to-aurora.ogg")
-----------------------------------------------------------------------------------------------------------------
ABOUT / INCLUDED IN PYGAME
* Built on top of the SDL (Simple Direct Media) to access audio, keyboar, mouse and graphics hardware.
-----------------------------------------------------------------------------------------------------------------
EVENTS
    import pygame
    import pygame.examples.eventlist as ev
    ev.main()
  - This list is useful to understand how Pygame handles events internally.
-----------------------------------------------------------------------------------------------------------------
STRUCTURE OF PYGAME APPLICATION
* Advised to start with a template.
* MODULES: Load any modules your game needs.
* EXTERNAL RESOURCES: Manage external resources. Load any sounds or images. If your game is played over the network, or it supports saving and loading from the file, this is where you'd handle it.
-----------------------------------------------------------------------------------------------------------------
BLITTING
* Old technical term (Bit Block Transfer)
* def. copying over all pixels from one surface to another. / The transfer of bits.
* The computer copies over all of the pixels in/from 'Surf' into 'Screen'
  - refer to file <Visual-Notes_0.py>
* GENERAL METHOD:
    target_surface.blit(Surface, (x,y))
  - Breakdown:
    - "target_surface": where we want to draw to
    - "Surface": where the information is coming from
    - "(x,y)": the coordinates for where on the target the source should be drawn
* Be mindful of blitting ORDER
  - The order in which you blit a surface determines the order in which they are displayed.
-----------------------------------------------------------------------------------------------------------------
UPDATING THE SCREEN
* Updating the program by adding a command relating the screen **only updates the Display's Surface**
* The computer must be told to update, as well, using either of the methods below:
  - pygame.display.flip() 
    - updates the whole screen
  - pygame.display.update() 
    - updates parts of the screen
* You will generally use the   update()   method due to the fact that updating the entire screen can take a lot of time and may cause lag.
   - The lag is seen especially when updating larger screens
-----------------------------------------------------------------------------------------------------------------
GRAPHIC COORDINATES -- computer graphics
* The origin of the screen, (0,0), is located at the top left
* x-axis, to the right
* y-axis, downward
