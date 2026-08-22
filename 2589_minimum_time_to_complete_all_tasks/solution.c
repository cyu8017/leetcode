// LeetCode 2589 - Minimum Time to Complete All Tasks
// https://leetcode.com/problems/minimum-time-to-complete-all-tasks/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

static int cmpTask(const void* a, const void* b) {
    int* ta = *(int**)a;
    int* tb = *(int**)b;
    return ta[1] - tb[1];
}

int findMinimumTime(int** tasks, int tasksSize, int* tasksColSize) {
    (void)tasksColSize;
    qsort(tasks, (size_t)tasksSize, sizeof(int*), cmpTask);
    bool used[2001];
    memset(used, 0, sizeof(used));
    int ans = 0;
    for (int t = 0; t < tasksSize; t++) {
        int start = tasks[t][0], end = tasks[t][1], dur = tasks[t][2];
        int have = 0;
        for (int i = start; i <= end; i++) if (used[i]) have++;
        int need = dur - have;
        for (int i = end; i >= start && need > 0; i--) {
            if (!used[i]) { used[i] = true; need--; ans++; }
        }
    }
    return ans;
}
