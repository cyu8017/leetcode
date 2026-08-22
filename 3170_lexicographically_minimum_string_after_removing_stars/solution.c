// LeetCode 3170 - Lexicographically Minimum String After Removing Stars
// https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

char* clearStars(char* s) {
    int n = (int)strlen(s);
    int* g[26];
    int glen[26] = {0}, gcap[26] = {0};
    for (int i = 0; i < 26; i++) g[i] = NULL;
    bool* rem = calloc(n, sizeof(bool));
    for (int i = 0; i < n; i++) {
        if (s[i] == '*') {
            rem[i] = true;
            for (int j = 0; j < 26; j++) {
                if (glen[j] > 0) {
                    rem[g[j][--glen[j]]] = true;
                    break;
                }
            }
        } else {
            int c = s[i] - 'a';
            if (glen[c] == gcap[c]) {
                gcap[c] = gcap[c] ? gcap[c] * 2 : 8;
                g[c] = realloc(g[c], gcap[c] * sizeof(int));
            }
            g[c][glen[c]++] = i;
        }
    }
    char* ans = malloc(n + 1);
    int p = 0;
    for (int i = 0; i < n; i++) if (!rem[i]) ans[p++] = s[i];
    ans[p] = 0;
    for (int i = 0; i < 26; i++) free(g[i]);
    free(rem);
    return ans;
}
