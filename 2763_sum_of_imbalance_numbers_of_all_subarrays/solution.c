// LeetCode 2763 - Sum of Imbalance Numbers of All Subarrays
// https://leetcode.com/problems/sum-of-imbalance-numbers-of-all-subarrays/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

int sumImbalanceNumbers(int* nums, int numsSize) {
    int n = numsSize;
    int ans = 0;
    int* sortedVals = (int*)malloc(n * sizeof(int));
    bool* seen = (bool*)malloc((n + 2) * sizeof(bool));
    for (int i = 0; i < n; i++) {
        memset(seen, 0, (n + 2) * sizeof(bool));
        int len = 0, imbalance = 0;
        for (int j = i; j < n; j++) {
            int x = nums[j];
            if (!seen[x]) {
                seen[x] = true;
                int pos = 0;
                while (pos < len && sortedVals[pos] < x) pos++;
                if (pos > 0) {
                    if (x - sortedVals[pos - 1] != 1) imbalance++;
                }
                if (pos < len) {
                    if (sortedVals[pos] - x != 1) imbalance++;
                }
                if (pos > 0 && pos < len) {
                    if (sortedVals[pos] - sortedVals[pos - 1] > 1) imbalance--;
                }
                for (int k = len; k > pos; k--) sortedVals[k] = sortedVals[k - 1];
                sortedVals[pos] = x;
                len++;
            }
            ans += imbalance;
        }
    }
    free(sortedVals); free(seen);
    return ans;
}
