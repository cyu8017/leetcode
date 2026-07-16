# How We Solve Trapping Rain Water

Bars trap rain between them. Count total water.

## Steps

1. Put left finger at start and right finger at end.
2. Track tallest bar seen on left and on right.
3. Move the finger at the **shorter** side inward.
4. If the bar is shorter than its side max, water += (side max - bar height).
5. Else update that side's max.
6. Repeat until fingers meet; return total water.
