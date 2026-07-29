// LeetCode 1101 - The Earliest Moment When Everyone Become Friends
// https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/

#include <stdlib.h>

static int cmpLogs(const void* a, const void* b) {
    const int* x = *(const int* const*)a;
    const int* y = *(const int* const*)b;
    return x[0] - y[0];
}

static int findParent(int* parent, int x) {
    while (parent[x] != x) {
        parent[x] = parent[parent[x]];
        x = parent[x];
    }
    return x;
}

int earliestAcq(int** logs, int logsSize, int* logsColSize, int n) {
    (void)logsColSize;
    int* parent = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) parent[i] = i;
    qsort(logs, (size_t)logsSize, sizeof(int*), cmpLogs);
    int components = n;
    for (int i = 0; i < logsSize; i++) {
        int a = findParent(parent, logs[i][1]);
        int b = findParent(parent, logs[i][2]);
        if (a != b) {
            parent[b] = a;
            components--;
            if (components == 1) {
                int t = logs[i][0];
                free(parent);
                return t;
            }
        }
    }
    free(parent);
    return -1;
}
