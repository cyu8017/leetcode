// LeetCode 1734 - Decode XORed Permutation
// https://leetcode.com/problems/decode-xored-permutation/

#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* decode(int* encoded, int encodedSize, int* returnSize) {
    int n = encodedSize + 1;
    int total = 0;
    for (int value = 1; value <= n; value++) {
        total ^= value;
    }
    int odd = 0;
    for (int i = 1; i < encodedSize; i += 2) {
        odd ^= encoded[i];
    }
    int* ans = (int*)malloc(n * sizeof(int));
    ans[0] = total ^ odd;
    for (int i = 0; i < encodedSize; i++) {
        ans[i + 1] = ans[i] ^ encoded[i];
    }
    *returnSize = n;
    return ans;
}
