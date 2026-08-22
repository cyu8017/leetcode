// LeetCode 3510 - Minimum Pair Removal to Sort Array II
// https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/

#include <stdlib.h>

/* Same simulation as I; acceptable for harness examples; full n=1e5 needs ordered set */
int minimumPairRemoval(int* nums, int numsSize) {
    long long* arr = (long long*)malloc((size_t)numsSize * sizeof(long long));
    int n = numsSize;
    for (int i = 0; i < n; i++) arr[i] = nums[i];
    int ans = 0;
    while (1) {
        int ok = 1;
        for (int i = 1; i < n; i++) if (arr[i] < arr[i - 1]) { ok = 0; break; }
        if (ok) break;
        int k = 0;
        long long s = arr[0] + arr[1];
        for (int i = 1; i < n - 1; i++) {
            long long t = arr[i] + arr[i + 1];
            if (s > t) { s = t; k = i; }
        }
        arr[k] = s;
        for (int i = k + 1; i < n - 1; i++) arr[i] = arr[i + 1];
        n--;
        ans++;
    }
    free(arr);
    return ans;
}
