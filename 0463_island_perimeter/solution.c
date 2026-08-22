// LeetCode 0463 - Island Perimeter
// https://leetcode.com/problems/island-perimeter/

int islandPerimeter(int** grid, int gridSize, int* gridColSize) {
    int perimeter = 0;
    int cols = gridColSize[0];
    for (int row = 0; row < gridSize; row++) {
        for (int col = 0; col < cols; col++) {
            if (grid[row][col] == 0) {
                continue;
            }
            perimeter += 4;
            if (row > 0 && grid[row - 1][col]) {
                perimeter -= 2;
            }
            if (col > 0 && grid[row][col - 1]) {
                perimeter -= 2;
            }
        }
    }
    return perimeter;
}
