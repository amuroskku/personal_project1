##Brick Breaker Game

This is a simple Brick Breaker game implemented in Python using the Pygame library.

## Features

- Classic brick breaker gameplay with paddle and ball mechanics
- Multiple levels with increasing difficulty
- Special items such as extra lives and additional balls (not fully implemented)
- Special bricks with effects 

## Installation

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).
2. Clone this repository to your local machine using `git clone`.
3. Install the required dependencies using `pip install -r requirements.txt`.

## Gameplay

- Use the left and right arrow keys to move the paddle.
- Break all the bricks on the screen using the ball without letting it fall below the paddle.
- Collect special items to gain extra lives or additional balls.
- Progress through multiple levels with increasing difficulty.

##Code Explanation

- `main.py`: This is the main Python script that runs the game. It contains the game loop, event handling, and rendering logic.
- `button.py`: This module defines the Button class, which handles the creation and interaction of buttons in the game interface.
- `ball.py`: This module defines the Ball class, which represents the game ball and its behavior.
- `brick.py`: This module defines the Brick class, which represents the bricks that the player must break to progress in the game.
- `paddle.py`: This module defines the Paddle class, which represents the player-controlled paddle at the bottom of the screen.
- `item.py`: This module defines the Item class, which represents special items that can be collected during gameplay, such as extra lives or additional balls.

