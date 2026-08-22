// LeetCode 2784 - Check if Array is Good
// https://leetcode.com/problems/check-if-array-is-good/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

bool isGood(int* nums, int numsSize) {
    int n = numsSize - 1;
    if (n < 1) return false;
    int* freq = (int*)calloc(n + 1, sizeof(int));
    for (int i = 0; i < numsSize; i++) {
        int v = nums[i];
        if (v < 1 || v > n) { free(freq); return false; }
        freq[v]++;
    }
    for (int i = 1; i < n; i++) {
        if (freq[i] != 1) { free(freq); return false; }
    }
    bool ok = freq[n] == 2;
    free(freq);
    return ok;
}
