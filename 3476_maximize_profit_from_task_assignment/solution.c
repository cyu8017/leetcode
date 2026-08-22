// LeetCode 3476 - Maximize Profit from Task Assignment
// https://leetcode.com/problems/maximize-profit-from-task-assignment/

#include <stdlib.h>

static int cmp_int(const void* a, const void* b) {
    int x = *(const int*)a, y = *(const int*)b;
    return (x > y) - (x < y);
}

static int cmp_task(const void* a, const void* b) {
    int* const* aa = (int* const*)a;
    int* const* bb = (int* const*)b;
    return ((*aa)[0] > (*bb)[0]) - ((*aa)[0] < (*bb)[0]);
}

long long maxProfit(int* workers, int workersSize, int** tasks, int tasksSize, int* tasksColSize) {
    (void)tasksColSize;
    qsort(workers, (size_t)workersSize, sizeof(int), cmp_int);
    qsort(tasks, (size_t)tasksSize, sizeof(int*), cmp_task);
    int* used = (int*)calloc((size_t)tasksSize, sizeof(int));
    long long ans = 0;
    for (int wi = 0; wi < workersSize; wi++) {
        int w = workers[wi];
        int best = -1, bi = -1;
        for (int i = 0; i < tasksSize; i++) {
            if (used[i]) continue;
            if (tasks[i][0] > w) break;
            if (tasks[i][1] > best) {
                best = tasks[i][1];
                bi = i;
            }
        }
        if (bi >= 0) {
            used[bi] = 1;
            ans += best;
        }
    }
    free(used);
    return ans;
}
