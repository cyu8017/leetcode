// LeetCode 2559 - Count Vowel Strings in Ranges
// https://leetcode.com/problems/count-vowel-strings-in-ranges/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

static bool isV(char c) {
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* vowelStrings(char** words, int wordsSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)queriesColSize;
    int* pref = (int*)calloc((size_t)(wordsSize + 1), sizeof(int));
    for (int i = 0; i < wordsSize; i++) {
        pref[i + 1] = pref[i];
        int len = (int)strlen(words[i]);
        if (len > 0 && isV(words[i][0]) && isV(words[i][len - 1])) pref[i + 1]++;
    }
    int* ans = (int*)malloc((size_t)queriesSize * sizeof(int));
    for (int i = 0; i < queriesSize; i++) {
        ans[i] = pref[queries[i][1] + 1] - pref[queries[i][0]];
    }
    free(pref);
    *returnSize = queriesSize;
    return ans;
}
