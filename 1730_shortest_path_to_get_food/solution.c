// LeetCode 1730 - Shortest Path to Get Food
// https://leetcode.com/problems/shortest-path-to-get-food/

#include <stdbool.h>
#include <stdlib.h>

int getFood(char** grid, int gridSize, int* gridColSize) {
    int rows = gridSize;
    int cols = gridColSize[0];
    int cells = rows * cols;
    int* queue = (int*)malloc(cells * 2 * sizeof(int));
    bool* seen = (bool*)calloc(cells, sizeof(bool));
    int head = 0;
    int tail = 0;
    for (int r = 0; r < rows; r++) {
        for (int c = 0; c < cols; c++) {
            if (grid[r][c] == '*') {
                queue[tail * 2] = r * cols + c;
                queue[tail * 2 + 1] = 0;
                tail++;
                seen[r * cols + c] = true;
            }
        }
    }
    const int dirs[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    int result = -1;
    while (head < tail) {
        int pos = queue[head * 2];
        int d = queue[head * 2 + 1];
        head++;
        int r = pos / cols;
        int c = pos % cols;
        if (grid[r][c] == '#') {
            result = d;
            break;
        }
        for (int i = 0; i < 4; i++) {
            int nr = r + dirs[i][0];
            int nc = c + dirs[i][1];
            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && !seen[nr * cols + nc] && grid[nr][nc] != 'X') {
                seen[nr * cols + nc] = true;
                queue[tail * 2] = nr * cols + nc;
                queue[tail * 2 + 1] = d + 1;
                tail++;
            }
        }
    }
    free(queue);
    free(seen);
    return result;
}
