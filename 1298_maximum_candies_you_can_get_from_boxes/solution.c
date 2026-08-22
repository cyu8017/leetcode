// LeetCode 1298 - Maximum Candies You Can Get from Boxes
// https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/

#include <stdlib.h>

typedef struct {
    int box;
} QNode;

int maxCandies(int* status, int statusSize, int* candies, int** keys, int* keysSize, int** containedBoxes, int* containedBoxesSize, int* initialBoxes, int initialBoxesSize) {
    (void)statusSize;
    (void)keysSize;
    (void)containedBoxesSize;
    int n = statusSize;
    int* owned = (int*)calloc((size_t)n, sizeof(int));
    int* opened = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < initialBoxesSize; i++) owned[initialBoxes[i]] = 1;
    QNode* queue = (QNode*)malloc((size_t)n * sizeof(QNode));
    int head = 0, tail = 0;
    for (int i = 0; i < initialBoxesSize; i++) {
        if (status[initialBoxes[i]]) queue[tail++] = (QNode){initialBoxes[i]};
    }
    int total = 0;
    while (head < tail) {
        int box = queue[head++].box;
        if (opened[box] || !status[box]) continue;
        opened[box] = 1;
        total += candies[box];
        for (int i = 0; i < keysSize[box]; i++) {
            int key = keys[box][i];
            status[key] = 1;
            if (owned[key] && !opened[key]) queue[tail++] = (QNode){key};
        }
        for (int i = 0; i < containedBoxesSize[box]; i++) {
            int child = containedBoxes[box][i];
            owned[child] = 1;
            if (status[child] && !opened[child]) queue[tail++] = (QNode){child};
        }
    }
    free(owned);
    free(opened);
    free(queue);
    return total;
}
