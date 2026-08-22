// LeetCode 3514 - Number of Unique XOR Triplets II
// https://leetcode.com/problems/number-of-unique-xor-triplets-ii/

#include <stdlib.h>
#include <string.h>

int uniqueXorTriplets(int* nums, int numsSize) {
    int mxv = nums[0];
    for (int i = 1; i < numsSize; i++) if (nums[i] > mxv) mxv = nums[i];
    int mx = mxv << 1;
    if (mx < 1) mx = 1;
    char* st = (char*)calloc((size_t)mx, 1);
    for (int i = 0; i < numsSize; i++)
        for (int j = 0; j < numsSize; j++) {
            int v = nums[i] ^ nums[j];
            if (v < mx) st[v] = 1;
        }
    int* s = (int*)calloc((size_t)mx, sizeof(int));
    for (int ab = 0; ab < mx; ab++) {
        if (!st[ab]) continue;
        for (int i = 0; i < numsSize; i++) {
            int v = ab ^ nums[i];
            if (v < mx) s[v] = 1;
        }
    }
    int ans = 0;
    for (int i = 0; i < mx; i++) ans += s[i];
    free(st); free(s);
    return ans;
}
