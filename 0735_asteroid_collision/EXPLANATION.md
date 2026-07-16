# How We Solve Asteroid Collision

Stack of surviving asteroids; collide when a right-mover meets a left-mover.

## Steps

1. Push positive (right-moving) asteroids freely.
2. On a negative asteroid, smash into stack tops while they are positive and smaller.
3. Equal sizes annihilate; otherwise the survivor stays.
