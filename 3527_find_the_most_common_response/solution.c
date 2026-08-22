// LeetCode 3527 - Find the Most Common Response
// https://leetcode.com/problems/find-the-most-common-response/

#include <stdlib.h>
#include <string.h>

char* findCommonResponse(char*** responses, int responsesSize, int* responsesColSize) {
    /* Collect unique words with counts - simple O(n^2) string compare table */
    char* words[10000];
    int cnt[10000];
    int wc = 0;
    for (int i = 0; i < responsesSize; i++) {
        for (int j = 0; j < responsesColSize[i]; j++) {
            char* w = responses[i][j];
            int dup = 0;
            for (int t = 0; t < j; t++) {
                if (strcmp(responses[i][t], w) == 0) { dup = 1; break; }
            }
            if (dup) continue;
            int found = -1;
            for (int t = 0; t < wc; t++) {
                if (strcmp(words[t], w) == 0) { found = t; break; }
            }
            if (found >= 0) cnt[found]++;
            else { words[wc] = w; cnt[wc] = 1; wc++; }
        }
    }
    char* ans = words[0];
    int best = cnt[0];
    for (int t = 1; t < wc; t++) {
        if (cnt[t] > best || (cnt[t] == best && strcmp(words[t], ans) < 0)) {
            best = cnt[t];
            ans = words[t];
        }
    }
    return ans;
}
