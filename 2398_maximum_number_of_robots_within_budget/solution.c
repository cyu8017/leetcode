// LeetCode 2398 - Maximum Number of Robots Within Budget
// https://leetcode.com/problems/maximum-number-of-robots-within-budget/

#include <stdlib.h>

int maximumRobots(int* chargeTimes, int chargeTimesSize, int* runningCosts, int runningCostsSize, long long budget) {
    (void)runningCostsSize;
    int n = chargeTimesSize, left = 0, ans = 0;
    long long sum = 0;
    int* dq = (int*)malloc((size_t)n * sizeof(int));
    int qh = 0, qt = 0;
    for (int right = 0; right < n; right++) {
        while (qh < qt && chargeTimes[dq[qt - 1]] <= chargeTimes[right]) qt--;
        dq[qt++] = right;
        sum += runningCosts[right];
        while (left <= right && (long long)chargeTimes[dq[qh]] + (long long)(right - left + 1) * sum > budget) {
            if (dq[qh] == left) qh++;
            sum -= runningCosts[left];
            left++;
        }
        if (right - left + 1 > ans) ans = right - left + 1;
    }
    free(dq);
    return ans;
}
