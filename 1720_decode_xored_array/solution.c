// LeetCode 1720 - Decode XORed Array
// https://leetcode.com/problems/decode-xored-array/

#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* decode(int* encoded, int encodedSize, int first, int* returnSize) {
    int* ans = (int*)malloc((encodedSize + 1) * sizeof(int));
    ans[0] = first;
    for (int i = 0; i < encodedSize; i++) {
        ans[i + 1] = ans[i] ^ encoded[i];
    }
    *returnSize = encodedSize + 1;
    return ans;
}
