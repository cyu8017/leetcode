// LeetCode 0490 - The Maze
// https://leetcode.com/problems/the-maze/

#include <stdbool.h>
#include <stdlib.h>

typedef struct {
    int row;
    int col;
} Point;

static bool pointContains(Point* points, int size, int row, int col) {
    for (int index = 0; index < size; index++) {
        if (points[index].row == row && points[index].col == col) {
            return true;
        }
    }
    return false;
}

static void pointAdd(Point** points, int* size, int* capacity, int row, int col) {
    if (*size >= *capacity) {
        *capacity = *capacity == 0 ? 16 : *capacity * 2;
        *points = (Point*)realloc(*points, (size_t)(*capacity) * sizeof(Point));
    }
    (*points)[*size].row = row;
    (*points)[(*size)++].col = col;
}

bool hasPath(int** maze, int mazeSize, int* mazeColSize, int* start, int startSize, int* destination,
             int destinationSize) {
    (void)startSize;
    (void)destinationSize;
    const int directions[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    Point* visited = NULL;
    int visitSize = 0;
    int visitCapacity = 0;
    Point* stack = NULL;
    int stackSize = 0;
    int stackCapacity = 0;
    pointAdd(&stack, &stackSize, &stackCapacity, start[0], start[1]);

    while (stackSize > 0) {
        Point current = stack[--stackSize];
        if (pointContains(visited, visitSize, current.row, current.col)) {
            continue;
        }
        pointAdd(&visited, &visitSize, &visitCapacity, current.row, current.col);
        if (current.row == destination[0] && current.col == destination[1]) {
            free(visited);
            free(stack);
            return true;
        }
        for (int index = 0; index < 4; index++) {
            int nextRow = current.row;
            int nextCol = current.col;
            while (nextRow + directions[index][0] >= 0 &&
                   nextRow + directions[index][0] < mazeSize &&
                   nextCol + directions[index][1] >= 0 &&
                   nextCol + directions[index][1] < mazeColSize[0] &&
                   maze[nextRow + directions[index][0]][nextCol + directions[index][1]] == 0) {
                nextRow += directions[index][0];
                nextCol += directions[index][1];
            }
            if (!pointContains(visited, visitSize, nextRow, nextCol)) {
                pointAdd(&stack, &stackSize, &stackCapacity, nextRow, nextCol);
            }
        }
    }
    free(visited);
    free(stack);
    return false;
}
