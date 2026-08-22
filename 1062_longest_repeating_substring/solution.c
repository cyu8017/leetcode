// LeetCode 1062 - Longest Repeating Substring
// https://leetcode.com/problems/longest-repeating-substring/

#include <stdlib.h>
#include <string.h>

int longestRepeatingSubstring(char* s) {
    int n = (int)strlen(s);
    int ans = 0;
    int* prev = (int*)calloc((size_t)n + 1, sizeof(int));
    int* cur = (int*)calloc((size_t)n + 1, sizeof(int));
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (s[i - 1] == s[j - 1] && i != j) {
                cur[j] = prev[j - 1] + 1;
                if (cur[j] > ans) {
                    ans = cur[j];
                }
            } else {
                cur[j] = 0;
            }
        }
        int* tmp = prev;
        prev = cur;
        cur = tmp;
        memset(cur, 0, ((size_t)n + 1) * sizeof(int));
    }
    free(prev);
    free(cur);
    return ans;
}
