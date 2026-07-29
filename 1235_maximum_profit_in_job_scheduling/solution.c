// LeetCode 1235 - Maximum Profit in Job Scheduling
// https://leetcode.com/problems/maximum-profit-in-job-scheduling/

#include <stdlib.h>

typedef struct {
    int end;
    int start;
    int profit;
} Job;

static int cmpJob(const void* a, const void* b) {
    const Job* x = (const Job*)a;
    const Job* y = (const Job*)b;
    return x->end - y->end;
}

static int upperBound(int* arr, int size, int target) {
    int lo = 0, hi = size;
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        if (arr[mid] <= target) lo = mid + 1;
        else hi = mid;
    }
    return lo;
}

int jobScheduling(int* startTime, int startTimeSize, int* endTime, int* profit, int profitSize) {
    (void)profitSize;
    Job* jobs = (Job*)malloc((size_t)startTimeSize * sizeof(Job));
    for (int i = 0; i < startTimeSize; i++) {
        jobs[i].end = endTime[i];
        jobs[i].start = startTime[i];
        jobs[i].profit = profit[i];
    }
    qsort(jobs, (size_t)startTimeSize, sizeof(Job), cmpJob);
    int* ends = (int*)malloc((size_t)(startTimeSize + 1) * sizeof(int));
    int* dp = (int*)malloc((size_t)(startTimeSize + 1) * sizeof(int));
    ends[0] = 0;
    dp[0] = 0;
    for (int i = 0; i < startTimeSize; i++) {
        ends[i + 1] = jobs[i].end;
        int j = upperBound(ends, i + 1, jobs[i].start) - 1;
        int withJob = dp[j] + jobs[i].profit;
        dp[i + 1] = dp[i] > withJob ? dp[i] : withJob;
    }
    int ans = dp[startTimeSize];
    free(jobs);
    free(ends);
    free(dp);
    return ans;
}
