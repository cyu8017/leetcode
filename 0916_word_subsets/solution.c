// LeetCode 0916 - Word Subsets
// https://leetcode.com/problems/word-subsets/

#include <stdlib.h>
#include <string.h>

char** wordSubsets(char** words1, int words1Size, char** words2, int words2Size, int* returnSize) {
    int need[26] = {0};
    for (int i = 0; i < words2Size; i++) {
        int cnt[26] = {0};
        for (char* p = words2[i]; *p; p++) cnt[*p - 'a']++;
        for (int c = 0; c < 26; c++) if (cnt[c] > need[c]) need[c] = cnt[c];
    }
    char** ans = (char**)malloc((size_t)words1Size * sizeof(char*));
    int n = 0;
    for (int i = 0; i < words1Size; i++) {
        int cnt[26] = {0};
        for (char* p = words1[i]; *p; p++) cnt[*p - 'a']++;
        int ok = 1;
        for (int c = 0; c < 26; c++) if (cnt[c] < need[c]) { ok = 0; break; }
        if (ok) ans[n++] = words1[i];
    }
    *returnSize = n;
    return ans;
}
