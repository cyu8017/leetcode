// LeetCode 1665 - Minimum Initial Energy to Finish Tasks
// https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/

#include <stdlib.h>

static int cmpTasks(const void* a, const void* b) {
    const int* x = *(const int* const*)a;
    const int* y = *(const int* const*)b;
    int dx = x[1] - x[0], dy = y[1] - y[0];
    return dy - dx;
}

int minimumEffort(int** tasks, int tasksSize, int* tasksColSize) {
    (void)tasksColSize;
    qsort(tasks, (size_t)tasksSize, sizeof(int*), cmpTasks);
    int energy = 0, spent = 0;
    for (int i = 0; i < tasksSize; i++) {
        int cost = tasks[i][0], minimum = tasks[i][1];
        int need = spent + minimum;
        if (need > energy) energy = need;
        spent += cost;
    }
    return energy;
}
