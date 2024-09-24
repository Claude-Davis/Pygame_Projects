INSTALLATION
* https://www.pygame.org/
-----------------------------------------------------------------------------------------------------------------
NEW PROJECT
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
ABOUT / INCLUDED
* Built on top of the SDL (Simple Direct Media) to access audio, keyboar, mouse and graphics hardware.
-----------------------------------------------------------------------------------------------------------------
* EVENTS
    import pygame
    import pygame.examples.eventlist as ev
    ev.main()
  - This list is useful to understand how Pygame handles events internally.
-----------------------------------------------------------------------------------------------------------------
STRUCTURE OF PYGAME APPLICATION
* Advised to start with a template.
* MODULES: Load any modules your game needs.
* EXTERNAL RESOURCES: Manage external resources. Load any sounds or images. If your game is played over the network, or it supports saving and loading from the file, this is where you'd handle it.
