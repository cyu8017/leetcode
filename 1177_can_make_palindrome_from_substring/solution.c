// LeetCode 1177 - Can Make Palindrome from Substring
// https://leetcode.com/problems/can-make-palindrome-from-substring/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

bool* canMakePaliQueries(char* s, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)queriesColSize;
    int n = (int)strlen(s);
    int* prefix = (int*)malloc((size_t)(n + 1) * sizeof(int));
    prefix[0] = 0;
    int mask = 0;
    for (int i = 0; i < n; i++) {
        mask ^= 1 << (s[i] - 'a');
        prefix[i + 1] = mask;
    }
    bool* ans = (bool*)malloc((size_t)queriesSize * sizeof(bool));
    for (int i = 0; i < queriesSize; i++) {
        int left = queries[i][0], right = queries[i][1], k = queries[i][2];
        int bits = prefix[right + 1] ^ prefix[left];
        int odd = 0;
        while (bits) { odd += bits & 1; bits >>= 1; }
        ans[i] = (odd / 2) <= k;
    }
    free(prefix);
    *returnSize = queriesSize;
    return ans;
}
