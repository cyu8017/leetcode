// LeetCode 1477 - Find Two Non-overlapping Sub-arrays Each With Target Sum
// https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/

#include <stdlib.h>

int minSumOfLengths(int* arr, int arrSize, int target) {
    int INF = 1000000000;
    int* shortest = (int*)malloc(arrSize * sizeof(int));
    int left = 0, total = 0, best = INF, ans = INF;
    for (int right = 0; right < arrSize; right++) {
        total += arr[right];
        while (total > target) total -= arr[left++];
        if (total == target) {
            int length = right - left + 1;
            if (left) {
                int cand = length + shortest[left - 1];
                if (cand < ans) ans = cand;
            }
            if (length < best) best = length;
        }
        shortest[right] = best;
    }
    free(shortest);
    return ans == INF ? -1 : ans;
}
