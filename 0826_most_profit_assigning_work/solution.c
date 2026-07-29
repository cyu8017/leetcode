// LeetCode 0826 - Most Profit Assigning Work
// https://leetcode.com/problems/most-profit-assigning-work/

#include <stdlib.h>

typedef struct { int d, p; } Job;

static int cmp_job(const void* a, const void* b) {
    return ((const Job*)a)->d - ((const Job*)b)->d;
}
static int cmp_int(const void* a, const void* b) {
    return (*(const int*)a) - (*(const int*)b);
}

#define MAX(a,b) ((a)>(b)?(a):(b))

int maxProfitAssignment(int* difficulty, int difficultySize, int* profit, int profitSize, int* worker, int workerSize) {
    (void)profitSize;
    Job* jobs = (Job*)malloc((size_t)difficultySize * sizeof(Job));
    for (int i = 0; i < difficultySize; i++) jobs[i] = (Job){difficulty[i], profit[i]};
    qsort(jobs, (size_t)difficultySize, sizeof(Job), cmp_job);
    qsort(worker, (size_t)workerSize, sizeof(int), cmp_int);
    int ans = 0, best = 0, i = 0;
    for (int w = 0; w < workerSize; w++) {
        while (i < difficultySize && jobs[i].d <= worker[w]) {
            best = MAX(best, jobs[i].p);
            i++;
        }
        ans += best;
    }
    free(jobs);
    return ans;
}
