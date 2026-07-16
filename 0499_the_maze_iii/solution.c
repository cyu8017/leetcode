// LeetCode 0499 - The Maze III
// https://leetcode.com/problems/the-maze-iii/

#include <limits.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int dist;
    char* path;
    int row;
    int col;
} State;

static int compareStates(const void* left, const void* right) {
    const State* a = (const State*)left;
    const State* b = (const State*)right;
    if (a->dist != b->dist) {
        return a->dist - b->dist;
    }
    return strcmp(a->path, b->path);
}

static void roll(int** maze, int mazeSize, int mazeColSize, int holeRow, int holeCol, int row,
                 int col, int dr, int dc, int* nextRow, int* nextCol, int* traveled) {
    *nextRow = row;
    *nextCol = col;
    *traveled = 0;
    while (*nextRow + dr >= 0 && *nextRow + dr < mazeSize && *nextCol + dc >= 0 &&
           *nextCol + dc < mazeColSize && maze[*nextRow + dr][*nextCol + dc] == 0) {
        *nextRow += dr;
        *nextCol += dc;
        (*traveled)++;
        if (*nextRow == holeRow && *nextCol == holeCol) {
            break;
        }
    }
}

char* findShortestWay(int** maze, int mazeSize, int* mazeColSize, int* ball, int ballSize,
                      int* hole, int holeSize) {
    (void)ballSize;
    (void)holeSize;
    const int rows = mazeSize;
    const int cols = mazeColSize[0];
    const int holeRow = hole[0];
    const int holeCol = hole[1];
    const int directions[4][2] = {{1, 0}, {0, -1}, {0, 1}, {-1, 0}};
    const char labels[4] = {'d', 'l', 'r', 'u'};

    int* bestDist = (int*)malloc((size_t)(rows * cols) * sizeof(int));
    char** bestPath = (char**)malloc((size_t)(rows * cols) * sizeof(char*));
    for (int index = 0; index < rows * cols; index++) {
        bestDist[index] = INT_MAX;
        bestPath[index] = NULL;
    }

    State* heap = (State*)malloc((size_t)(rows * cols * 4) * sizeof(State));
    int heapSize = 0;
    heap[heapSize].dist = 0;
    heap[heapSize].path = strdup("");
    heap[heapSize].row = ball[0];
    heap[heapSize].col = ball[1];
    heapSize++;

    char* answer = NULL;
    while (heapSize > 0) {
        qsort(heap, (size_t)heapSize, sizeof(State), compareStates);
        State current = heap[0];
        heap[0] = heap[--heapSize];
        const int stateIndex = current.row * cols + current.col;
        if (bestDist[stateIndex] < current.dist ||
            (bestDist[stateIndex] == current.dist && bestPath[stateIndex] &&
             strcmp(bestPath[stateIndex], current.path) <= 0)) {
            free(current.path);
            continue;
        }
        bestDist[stateIndex] = current.dist;
        free(bestPath[stateIndex]);
        bestPath[stateIndex] = current.path;

        if (current.row == holeRow && current.col == holeCol) {
            answer = strdup(current.path);
            break;
        }

        for (int index = 0; index < 4; index++) {
            int nextRow;
            int nextCol;
            int traveled;
            roll(maze, mazeSize, cols, holeRow, holeCol, current.row, current.col,
                 directions[index][0], directions[index][1], &nextRow, &nextCol, &traveled);
            if (nextRow == current.row && nextCol == current.col) {
                continue;
            }
            const int newDist = current.dist + traveled;
            char label[2] = {labels[index], '\0'};
            char* newPath = (char*)malloc(strlen(current.path) + 2);
            strcpy(newPath, current.path);
            strcat(newPath, label);
            const int targetIndex = nextRow * cols + nextCol;
            if (newDist < bestDist[targetIndex] ||
                (newDist == bestDist[targetIndex] && bestPath[targetIndex] &&
                 strcmp(newPath, bestPath[targetIndex]) < 0) ||
                bestPath[targetIndex] == NULL) {
                heap[heapSize].dist = newDist;
                heap[heapSize].path = newPath;
                heap[heapSize].row = nextRow;
                heap[heapSize].col = nextCol;
                heapSize++;
            } else {
                free(newPath);
            }
        }
    }

    for (int index = 0; index < rows * cols; index++) {
        free(bestPath[index]);
    }
    free(bestPath);
    free(bestDist);
    free(heap);
    return answer ? answer : strdup("impossible");
}
