// LeetCode 2817 - Minimum Absolute Difference Between Elements With Constraint
// https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/

#include <stdlib.h>
#include <limits.h>

int minAbsoluteDifference(int* nums, int numsSize, int x) {
    if (x == 0) {
        int ans = INT_MAX;
        for (int i = 1; i < numsSize; i++) {
            int d = nums[i] - nums[i - 1];
            if (d < 0) d = -d;
            if (d < ans) ans = d;
        }
        return ans;
    }
    int ans = INT_MAX;
    int* arr = (int*)malloc(numsSize * sizeof(int));
    int len = 0;
    for (int i = x; i < numsSize; i++) {
        int v = nums[i - x];
        int pos = 0;
        while (pos < len && arr[pos] < v) pos++;
        for (int k = len; k > pos; k--) arr[k] = arr[k - 1];
        arr[pos] = v;
        len++;
        int cur = nums[i];
        int lo = 0, hi = len;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (arr[mid] < cur) lo = mid + 1;
            else hi = mid;
        }
        int p = lo;
        if (p < len) {
            int d = arr[p] - cur;
            if (d < ans) ans = d;
        }
        if (p > 0) {
            int d = cur - arr[p - 1];
            if (d < ans) ans = d;
        }
    }
    free(arr);
    return ans;
}
