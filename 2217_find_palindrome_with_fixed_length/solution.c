// LeetCode 2217 - Find Palindrome With Fixed Length
// https://leetcode.com/problems/find-palindrome-with-fixed-length/

#include <stdlib.h>

long long* kthPalindrome(int* queries, int queriesSize, int intLength, int* returnSize) {
    int half = (intLength + 1) / 2;
    int start = 1;
    for (int i = 1; i < half; i++) start *= 10;
    int total = start * 9;
    long long* ans = (long long*)malloc((size_t)queriesSize * sizeof(long long));
    for (int i = 0; i < queriesSize; i++) {
        int q = queries[i];
        if (q > total) { ans[i] = -1; continue; }
        int left = start + q - 1;
        long long pal = left;
        int x = left;
        if (intLength % 2 == 1) x /= 10;
        while (x > 0) { pal = pal * 10 + x % 10; x /= 10; }
        ans[i] = pal;
    }
    *returnSize = queriesSize;
    return ans;
}
