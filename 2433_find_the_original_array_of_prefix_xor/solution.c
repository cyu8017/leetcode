// LeetCode 2433 - Find The Original Array of Prefix Xor
// https://leetcode.com/problems/find-the-original-array-of-prefix-xor/

#include <stdlib.h>

int* findArray(int* pref, int prefSize, int* returnSize) {
    int* ans = (int*)malloc((size_t)prefSize * sizeof(int));
    ans[0] = pref[0];
    for (int i = 1; i < prefSize; i++) ans[i] = pref[i] ^ pref[i - 1];
    *returnSize = prefSize;
    return ans;
}
