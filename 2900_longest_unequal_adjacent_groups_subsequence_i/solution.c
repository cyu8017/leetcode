// LeetCode 2900 - Longest Unequal Adjacent Groups Subsequence I
// https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/

#include <stdlib.h>
#include <string.h>

char** getLongestSubsequence(char** words, int wordsSize, int* groups, int groupsSize, int* returnSize) {
    (void)groupsSize;
    char** ans = (char**)malloc(wordsSize * sizeof(char*));
    int an = 0;
    ans[an++] = words[0];
    int last = groups[0];
    for (int i = 1; i < wordsSize; i++) {
        if (groups[i] != last) { ans[an++] = words[i]; last = groups[i]; }
    }
    *returnSize = an;
    return ans;
}
