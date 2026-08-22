// LeetCode 2901 - Longest Unequal Adjacent Groups Subsequence II
// https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/

#include <stdlib.h>
#include <string.h>

static int hamming(const char* a, const char* b) {
    int la = (int)strlen(a), lb = (int)strlen(b);
    if (la != lb) return 100;
    int d = 0;
    for (int i = 0; i < la; i++) if (a[i] != b[i]) d++;
    return d;
}

char** getWordsInLongestSubsequence(char** words, int wordsSize, int* groups, int groupsSize, int* returnSize) {
    (void)groupsSize;
    int n = wordsSize;
    int* dp = (int*)malloc(n * sizeof(int));
    int* prev = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) { dp[i] = 1; prev[i] = -1; }
    int best = 1, bestI = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (groups[i] != groups[j] && hamming(words[i], words[j]) == 1 && dp[j] + 1 > dp[i]) {
                dp[i] = dp[j] + 1;
                prev[i] = j;
            }
        }
        if (dp[i] > best) { best = dp[i]; bestI = i; }
    }
    char** path = (char**)malloc(best * sizeof(char*));
    int pn = 0;
    for (int cur = bestI; cur != -1; cur = prev[cur]) path[pn++] = words[cur];
    for (int i = 0, j = pn - 1; i < j; i++, j--) { char* t = path[i]; path[i] = path[j]; path[j] = t; }
    free(dp); free(prev);
    *returnSize = pn;
    return path;
}
