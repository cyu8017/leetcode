# How We Solve Battleships in a Board

Count ship heads only at cells with no X above or left.

## Steps

1. Scan every board cell.
2. Ignore X cells that continue a ship horizontally or vertically.
3. Count each remaining X as one battleship.
