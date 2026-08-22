// LeetCode 3474 - Lexicographically Smallest Generated String
// https://leetcode.com/problems/lexicographically-smallest-generated-string/

#include <stdlib.h>
#include <string.h>

char* generateString(char* str1, char* str2) {
    int n = (int)strlen(str1);
    int m = (int)strlen(str2);
    int L = n + m - 1;
    char* ans = (char*)malloc((size_t)L + 1);
    for (int i = 0; i < L; i++) ans[i] = '?';
    ans[L] = '\0';
    for (int i = 0; i < n; i++) {
        if (str1[i] == 'T') {
            for (int j = 0; j < m; j++) {
                if (ans[i + j] != '?' && ans[i + j] != str2[j]) {
                    free(ans);
                    char* empty = (char*)malloc(1);
                    empty[0] = '\0';
                    return empty;
                }
                ans[i + j] = str2[j];
            }
        }
    }
    for (int i = 0; i < L; i++) {
        if (ans[i] == '?') ans[i] = 'a';
    }
    for (int i = 0; i < n; i++) {
        if (str1[i] == 'F') {
            int match = 1;
            for (int j = 0; j < m; j++) {
                if (ans[i + j] != str2[j]) {
                    match = 0;
                    break;
                }
            }
            if (match) {
                int changed = 0;
                for (int j = m - 1; j >= 0; j--) {
                    int pos = i + j;
                    int forced = 0;
                    for (int t = 0; t < n; t++) {
                        if (str1[t] == 'T' && pos >= t && pos < t + m) {
                            forced = 1;
                            break;
                        }
                    }
                    if (!forced) {
                        ans[pos] = 'b';
                        changed = 1;
                        break;
                    }
                }
                if (!changed) {
                    free(ans);
                    char* empty = (char*)malloc(1);
                    empty[0] = '\0';
                    return empty;
                }
            }
        }
    }
    for (int i = 0; i < n; i++) {
        int match = 1;
        for (int j = 0; j < m; j++) {
            if (ans[i + j] != str2[j]) {
                match = 0;
                break;
            }
        }
        if (str1[i] == 'T' && !match) {
            free(ans);
            char* empty = (char*)malloc(1);
            empty[0] = '\0';
            return empty;
        }
        if (str1[i] == 'F' && match) {
            free(ans);
            char* empty = (char*)malloc(1);
            empty[0] = '\0';
            return empty;
        }
    }
    return ans;
}
