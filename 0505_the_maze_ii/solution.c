// LeetCode 0505 - The Maze II
// https://leetcode.com/problems/the-maze-ii/

#include <limits.h>
#include <stdlib.h>

typedef struct {
    int dist;
    int row;
    int col;
} State;

static int compareStates(const void* leftPtr, const void* rightPtr) {
    const State* left = (const State*)leftPtr;
    const State* right = (const State*)rightPtr;
    return left->dist - right->dist;
}

static void roll(int** maze, int rows, int cols, int row, int col, int dr, int dc, int* nextRow,
                 int* nextCol, int* traveled) {
    *nextRow = row;
    *nextCol = col;
    *traveled = 0;
    while (*nextRow + dr >= 0 && *nextRow + dr < rows && *nextCol + dc >= 0 &&
           *nextCol + dc < cols && maze[*nextRow + dr][*nextCol + dc] == 0) {
        *nextRow += dr;
        *nextCol += dc;
        (*traveled)++;
    }
}

int shortestDistance(int** maze, int mazeSize, int* mazeColSize, int* start, int startSize,
                     int* destination, int destinationSize) {
    (void)startSize;
    (void)destinationSize;
    const int rows = mazeSize;
    const int cols = mazeColSize[0];
    const int targetRow = destination[0];
    const int targetCol = destination[1];
    const int directions[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    int* best = (int*)malloc((size_t)(rows * cols) * sizeof(int));
    for (int index = 0; index < rows * cols; index++) {
        best[index] = INT_MAX;
    }

    State* heap = (State*)malloc((size_t)(rows * cols * 4) * sizeof(State));
    int heapSize = 0;
    heap[heapSize].dist = 0;
    heap[heapSize].row = start[0];
    heap[heapSize].col = start[1];
    heapSize++;

    int answer = -1;
    while (heapSize > 0) {
        qsort(heap, (size_t)heapSize, sizeof(State), compareStates);
        State current = heap[0];
        heap[0] = heap[--heapSize];
        const int stateIndex = current.row * cols + current.col;
        if (current.row == targetRow && current.col == targetCol) {
            answer = current.dist;
            break;
        }
        if (best[stateIndex] <= current.dist) {
            continue;
        }
        best[stateIndex] = current.dist;

        for (int index = 0; index < 4; index++) {
            int nextRow;
            int nextCol;
            int traveled;
            roll(maze, rows, cols, current.row, current.col, directions[index][0],
                 directions[index][1], &nextRow, &nextCol, &traveled);
            if (nextRow == current.row && nextCol == current.col) {
                continue;
            }
            const int newDist = current.dist + traveled;
            const int targetIndex = nextRow * cols + nextCol;
            if (newDist < best[targetIndex]) {
                heap[heapSize].dist = newDist;
                heap[heapSize].row = nextRow;
                heap[heapSize].col = nextCol;
                heapSize++;
            }
        }
    }

    free(best);
    free(heap);
    return answer;
}
