// LeetCode 2904 - Shortest and Lexicographically Smallest Beautiful String
// https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/

#include <stdlib.h>
#include <string.h>

char* shortestBeautifulSubstring(char* s, int k) {
    int n = (int)strlen(s);
    char* ans = (char*)calloc(1, 1);
    for (int i = 0; i < n; i++) {
        int ones = 0;
        for (int j = i; j < n; j++) {
            if (s[j] == '1') ones++;
            if (ones == k) {
                int len = j - i + 1;
                char* cand = (char*)malloc(len + 1);
                memcpy(cand, s + i, len); cand[len] = '\0';
                if (ans[0] == '\0' || len < (int)strlen(ans) || (len == (int)strlen(ans) && strcmp(cand, ans) < 0)) {
                    free(ans); ans = cand;
                } else free(cand);
                break;
            }
            if (ones > k) break;
        }
    }
    return ans;
}
