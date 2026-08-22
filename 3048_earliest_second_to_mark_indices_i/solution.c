// LeetCode 3048 - Earliest Second to Mark Indices I
// https://leetcode.com/problems/earliest-second-to-mark-indices-i/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

static bool check(int* nums, int n, int* changeIndices, int t) {
    int* last = (int*)calloc((size_t)(n + 1), sizeof(int));
    for (int s = 0; s < t; s++) last[changeIndices[s]] = s;
    int decrement = 0, marked = 0;
    for (int s = 0; s < t; s++) {
        int i = changeIndices[s];
        if (last[i] == s) {
            if (decrement < nums[i - 1]) { free(last); return false; }
            decrement -= nums[i - 1];
            marked++;
        } else decrement++;
    }
    free(last);
    return marked == n;
}

int earliestSecondToMarkIndices(int* nums, int numsSize, int* changeIndices, int changeIndicesSize) {
    int n = numsSize, m = changeIndicesSize;
    int l = 0, r = m + 1;
    while (l < r) {
        int mid = (l + r) / 2;
        if (check(nums, n, changeIndices, mid)) r = mid;
        else l = mid + 1;
    }
    return l > m ? -1 : l;
}
