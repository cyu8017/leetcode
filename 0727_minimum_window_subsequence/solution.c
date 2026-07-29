// LeetCode 0727 - Minimum Window Subsequence
// https://leetcode.com/problems/minimum-window-subsequence/

#include <stdlib.h>
#include <string.h>

char* minWindow(char* s1, char* s2) {
    int m = (int)strlen(s1);
    int n = (int)strlen(s2);
    char* best = (char*)malloc(1);
    best[0] = '\0';
    int i = 0;
    while (i < m) {
        int j = 0;
        int k = i;
        while (k < m && j < n) {
            if (s1[k] == s2[j]) {
                j++;
            }
            k++;
        }
        if (j < n) {
            break;
        }
        int end = k - 1;
        j = n - 1;
        k = end;
        while (j >= 0) {
            if (s1[k] == s2[j]) {
                j--;
            }
            k--;
        }
        int start = k + 1;
        int len = end - start + 1;
        if (best[0] == '\0' || len < (int)strlen(best)) {
            free(best);
            best = (char*)malloc((size_t)len + 1);
            memcpy(best, s1 + start, (size_t)len);
            best[len] = '\0';
        }
        i = start + 1;
    }
    return best;
}
