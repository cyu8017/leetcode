// LeetCode 0542 - 01 Matrix
// https://leetcode.com/problems/01-matrix/

#include <limits.h>
#include <stdlib.h>

typedef struct {
    int row;
    int col;
} Cell;

int** updateMatrix(int** mat, int matSize, int* matColSize, int* returnSize, int** returnColumnSizes) {
    const int rows = matSize;
    const int cols = matColSize[0];
    const int inf = 1000000000;

    int** dist = (int**)malloc((size_t)rows * sizeof(int*));
    *returnSize = rows;
    *returnColumnSizes = (int*)malloc((size_t)rows * sizeof(int));

    Cell* queue = (Cell*)malloc((size_t)rows * (size_t)cols * sizeof(Cell));
    int front = 0;
    int rear = 0;

    for (int row = 0; row < rows; row++) {
        dist[row] = (int*)malloc((size_t)cols * sizeof(int));
        (*returnColumnSizes)[row] = cols;
        for (int col = 0; col < cols; col++) {
            if (mat[row][col] == 0) {
                dist[row][col] = 0;
                queue[rear].row = row;
                queue[rear].col = col;
                rear++;
            } else {
                dist[row][col] = inf;
            }
        }
    }

    const int directions[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    while (front < rear) {
        const int row = queue[front].row;
        const int col = queue[front].col;
        front++;
        for (int index = 0; index < 4; index++) {
            const int nextRow = row + directions[index][0];
            const int nextCol = col + directions[index][1];
            if (nextRow >= 0 && nextRow < rows && nextCol >= 0 && nextCol < cols &&
                dist[nextRow][nextCol] > dist[row][col] + 1) {
                dist[nextRow][nextCol] = dist[row][col] + 1;
                queue[rear].row = nextRow;
                queue[rear].col = nextCol;
                rear++;
            }
        }
    }

    free(queue);
    return dist;
}
