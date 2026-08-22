// LeetCode 2323 - Find Minimum Time to Finish All Jobs II
// https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs-ii/

#include <stdlib.h>

static int cmp_int(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int minimumTime(int* jobs, int jobsSize, int* workers, int workersSize) {
    (void)workersSize;
    qsort(jobs, (size_t)jobsSize, sizeof(int), cmp_int);
    qsort(workers, (size_t)jobsSize, sizeof(int), cmp_int);
    int ans = 0;
    for (int i = 0; i < jobsSize; i++) {
        int days = (jobs[i] + workers[i] - 1) / workers[i];
        if (days > ans) ans = days;
    }
    return ans;
}
