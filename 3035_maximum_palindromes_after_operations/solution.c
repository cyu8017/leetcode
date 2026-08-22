// LeetCode 3035 - Maximum Palindromes After Operations
// https://leetcode.com/problems/maximum-palindromes-after-operations/

#include <stdlib.h>
#include <string.h>

static int popcount(unsigned x) {
    int c = 0; while (x) { c += x & 1; x >>= 1; } return c;
}
static int cmp_len(const void* a, const void* b) {
    const char* sa = *(const char* const*)a;
    const char* sb = *(const char* const*)b;
    return (int)strlen(sa) - (int)strlen(sb);
}

int maxPalindromesAfterOperations(char** words, int wordsSize) {
    int s = 0; unsigned mask = 0;
    for (int i = 0; i < wordsSize; i++) {
        s += (int)strlen(words[i]);
        for (int j = 0; words[i][j]; j++) mask ^= 1u << (words[i][j] - 'a');
    }
    s -= popcount(mask);
    qsort(words, (size_t)wordsSize, sizeof(char*), cmp_len);
    int ans = 0;
    for (int i = 0; i < wordsSize; i++) {
        int len = (int)strlen(words[i]);
        s -= (len / 2) * 2;
        if (s < 0) break;
        ans++;
    }
    return ans;
}
