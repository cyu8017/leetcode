// LeetCode 0286 - Walls and Gates
// https://leetcode.com/problems/walls-and-gates/

#include <limits.h>
#include <stdlib.h>

typedef struct {
    int row;
    int col;
} Cell;

typedef struct {
    Cell* data;
    int front;
    int back;
    int capacity;
} Queue;

static void queueInit(Queue* queue) {
    queue->capacity = 64;
    queue->data = (Cell*)malloc((size_t)queue->capacity * sizeof(Cell));
    queue->front = 0;
    queue->back = 0;
}

static void queuePush(Queue* queue, Cell cell) {
    if (queue->back >= queue->capacity) {
        queue->capacity *= 2;
        queue->data = (Cell*)realloc(queue->data, (size_t)queue->capacity * sizeof(Cell));
    }
    queue->data[queue->back++] = cell;
}

static bool queueEmpty(Queue* queue) {
    return queue->front >= queue->back;
}

static Cell queuePop(Queue* queue) {
    return queue->data[queue->front++];
}

static void queueFree(Queue* queue) {
    free(queue->data);
}

void wallsAndGates(int** rooms, int roomsSize, int* roomsColSize) {
    if (roomsSize == 0 || roomsColSize[0] == 0) {
        return;
    }

    int rows = roomsSize;
    int cols = roomsColSize[0];
    Queue queue;
    queueInit(&queue);

    for (int row = 0; row < rows; row++) {
        for (int col = 0; col < cols; col++) {
            if (rooms[row][col] == 0) {
                queuePush(&queue, (Cell){row, col});
            }
        }
    }

    const int directions[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    while (!queueEmpty(&queue)) {
        Cell current = queuePop(&queue);
        for (int index = 0; index < 4; index++) {
            int nextRow = current.row + directions[index][0];
            int nextCol = current.col + directions[index][1];
            if (nextRow >= 0 && nextRow < rows && nextCol >= 0 && nextCol < cols &&
                rooms[nextRow][nextCol] == INT_MAX) {
                rooms[nextRow][nextCol] = rooms[current.row][current.col] + 1;
                queuePush(&queue, (Cell){nextRow, nextCol});
            }
        }
    }

    queueFree(&queue);
}
