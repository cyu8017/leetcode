// LeetCode 0317 - Shortest Distance from All Buildings
// https://leetcode.com/problems/shortest-distance-from-all-buildings/

#include <limits.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int row;
    int col;
    int distance;
} QueueEntry;

int shortestDistance(int** grid, int gridSize, int* gridColSize) {
    if (gridSize == 0) {
        return -1;
    }

    int rows = gridSize;
    int cols = gridColSize[0];
    int buildings = 0;
    for (int row = 0; row < rows; row++) {
        for (int col = 0; col < cols; col++) {
            if (grid[row][col] == 1) {
                buildings += 1;
            }
        }
    }

    int** distances = (int**)malloc((size_t)rows * sizeof(int*));
    int** reach = (int**)malloc((size_t)rows * sizeof(int*));
    bool** visited = (bool**)malloc((size_t)rows * sizeof(bool*));
    for (int row = 0; row < rows; row++) {
        distances[row] = (int*)calloc((size_t)cols, sizeof(int));
        reach[row] = (int*)calloc((size_t)cols, sizeof(int));
        visited[row] = (bool*)calloc((size_t)cols, sizeof(bool));
    }

    QueueEntry* queue = (QueueEntry*)malloc((size_t)rows * cols * sizeof(QueueEntry));
    const int directions[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    for (int row = 0; row < rows; row++) {
        for (int col = 0; col < cols; col++) {
            if (grid[row][col] != 1) {
                continue;
            }
            for (int visitRow = 0; visitRow < rows; visitRow++) {
                memset(visited[visitRow], 0, (size_t)cols * sizeof(bool));
            }
            int front = 0;
            int rear = 0;
            queue[rear++] = (QueueEntry){row, col, 0};
            visited[row][col] = true;
            while (front < rear) {
                QueueEntry entry = queue[front++];
                for (int direction = 0; direction < 4; direction++) {
                    int nextRow = entry.row + directions[direction][0];
                    int nextCol = entry.col + directions[direction][1];
                    if (nextRow >= 0 && nextRow < rows && nextCol >= 0 && nextCol < cols
                        && grid[nextRow][nextCol] == 0 && !visited[nextRow][nextCol]) {
                        visited[nextRow][nextCol] = true;
                        distances[nextRow][nextCol] += entry.distance + 1;
                        reach[nextRow][nextCol] += 1;
                        queue[rear++] = (QueueEntry){nextRow, nextCol, entry.distance + 1};
                    }
                }
            }
        }
    }

    int best = INT_MAX;
    for (int row = 0; row < rows; row++) {
        for (int col = 0; col < cols; col++) {
            if (grid[row][col] == 0 && reach[row][col] == buildings) {
                if (distances[row][col] < best) {
                    best = distances[row][col];
                }
            }
        }
    }

    for (int row = 0; row < rows; row++) {
        free(distances[row]);
        free(reach[row]);
        free(visited[row]);
    }
    free(distances);
    free(reach);
    free(visited);
    free(queue);
    return best == INT_MAX ? -1 : best;
}
