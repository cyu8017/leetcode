// LeetCode 0862 - Shortest Subarray with Sum at Least K
// https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

#include <stdlib.h>

#define MIN(a,b) ((a)<(b)?(a):(b))

int shortestSubarray(int* nums, int numsSize, int k) {
    int n = numsSize;
    long long* prefix = (long long*)malloc((size_t)(n + 1) * sizeof(long long));
    prefix[0] = 0;
    for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + nums[i];
    int* dq = (int*)malloc((size_t)(n + 1) * sizeof(int));
    int head = 0, tail = 0;
    int ans = n + 1;
    for (int i = 0; i <= n; i++) {
        while (head < tail && prefix[i] - prefix[dq[head]] >= k) {
            ans = MIN(ans, i - dq[head]);
            head++;
        }
        while (head < tail && prefix[i] <= prefix[dq[tail - 1]]) tail--;
        dq[tail++] = i;
    }
    free(prefix); free(dq);
    return ans <= n ? ans : -1;
}
