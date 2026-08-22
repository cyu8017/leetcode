// LeetCode 2071 - Maximum Number of Tasks You Can Assign
// https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

static int cmpInt(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }

static bool can2071(int k, int* tasks, int* workers, int workersSize, int pills, int strength) {
    if (k == 0) return true;
    int* ws = (int*)malloc((size_t)k * sizeof(int));
    memcpy(ws, workers + workersSize - k, (size_t)k * sizeof(int));
    int wn = k, p = pills;
    for (int i = k - 1; i >= 0; i--) {
        int task = tasks[i];
        if (ws[wn - 1] >= task) { wn--; continue; }
        if (p == 0) { free(ws); return false; }
        int lo = 0, hi = wn;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (ws[mid] + strength >= task) hi = mid;
            else lo = mid + 1;
        }
        if (lo == wn) { free(ws); return false; }
        for (int j = lo; j + 1 < wn; j++) ws[j] = ws[j + 1];
        wn--;
        p--;
    }
    free(ws);
    return true;
}

int maxTaskAssign(int* tasks, int tasksSize, int* workers, int workersSize, int pills, int strength) {
    qsort(tasks, (size_t)tasksSize, sizeof(int), cmpInt);
    qsort(workers, (size_t)workersSize, sizeof(int), cmpInt);
    int lo = 0, hi = tasksSize < workersSize ? tasksSize : workersSize;
    while (lo < hi) {
        int mid = (lo + hi + 1) / 2;
        if (can2071(mid, tasks, workers, workersSize, pills, strength)) lo = mid;
        else hi = mid - 1;
    }
    return lo;
}
