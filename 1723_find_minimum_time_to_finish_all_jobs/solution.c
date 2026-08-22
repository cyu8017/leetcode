// LeetCode 1723 - Find Minimum Time to Finish All Jobs
// https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/

#include <stdbool.h>
#include <stdlib.h>

static int compareDesc(const void* a, const void* b) {
    int va = *(const int*)a;
    int vb = *(const int*)b;
    return (va < vb) - (va > vb);
}

static void backtrack(int i, const int* jobs, int jobsSize, int* loads, int k, int* best) {
    if (i == jobsSize) {
        int max = 0;
        for (int worker = 0; worker < k; worker++) {
            if (loads[worker] > max) {
                max = loads[worker];
            }
        }
        if (max < *best) {
            *best = max;
        }
        return;
    }
    for (int worker = 0; worker < k; worker++) {
        bool seen = false;
        for (int prev = 0; prev < worker; prev++) {
            if (loads[prev] == loads[worker]) {
                seen = true;
                break;
            }
        }
        if (seen) {
            continue;
        }
        if (loads[worker] + jobs[i] >= *best) {
            continue;
        }
        loads[worker] += jobs[i];
        backtrack(i + 1, jobs, jobsSize, loads, k, best);
        loads[worker] -= jobs[i];
        if (loads[worker] == 0) {
            break;
        }
    }
}

int minimumTimeRequired(int* jobs, int jobsSize, int k) {
    qsort(jobs, jobsSize, sizeof(int), compareDesc);
    int* loads = (int*)calloc(k, sizeof(int));
    int best = 0;
    for (int i = 0; i < jobsSize; i++) {
        best += jobs[i];
    }
    backtrack(0, jobs, jobsSize, loads, k, &best);
    free(loads);
    return best;
}
