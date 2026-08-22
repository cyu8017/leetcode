// LeetCode 2781 - Length of the Longest Valid Substring
// https://leetcode.com/problems/length-of-the-longest-valid-substring/

#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

int longestValidSubstring(char* word, char** forbidden, int forbiddenSize) {
    int maxLen = 0;
    for (int i = 0; i < forbiddenSize; i++) {
        int L = (int)strlen(forbidden[i]);
        if (L > maxLen) maxLen = L;
    }
    int n = (int)strlen(word);
    int ans = 0, right = n - 1;
    for (int left = n - 1; left >= 0; left--) {
        for (int k = left; k <= right && k - left + 1 <= maxLen; k++) {
            int len = k - left + 1;
            bool hit = false;
            for (int f = 0; f < forbiddenSize; f++) {
                if ((int)strlen(forbidden[f]) == len && strncmp(word + left, forbidden[f], len) == 0) {
                    hit = true; break;
                }
            }
            if (hit) { right = k - 1; break; }
        }
        if (right - left + 1 > ans) ans = right - left + 1;
    }
    return ans;
}
