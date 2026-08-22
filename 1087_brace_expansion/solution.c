// LeetCode 1087 - Brace Expansion
// https://leetcode.com/problems/brace-expansion/

#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** expand(char* s, int* returnSize) {
    char groups[100][26];
    int groupSizes[100];
    int groupCount = 0;
    int i = 0;
    int n = (int)strlen(s);
    while (i < n) {
        if (s[i] == '{') {
            i++;
            int gsize = 0;
            while (s[i] != '}') {
                if (s[i] != ',') {
                    groups[groupCount][gsize++] = s[i];
                }
                i++;
            }
            // sort group letters
            for (int a = 0; a < gsize; a++) {
                for (int b = a + 1; b < gsize; b++) {
                    if (groups[groupCount][b] < groups[groupCount][a]) {
                        char t = groups[groupCount][a];
                        groups[groupCount][a] = groups[groupCount][b];
                        groups[groupCount][b] = t;
                    }
                }
            }
            groupSizes[groupCount++] = gsize;
            i++;
        } else {
            groups[groupCount][0] = s[i];
            groupSizes[groupCount++] = 1;
            i++;
        }
    }

    char** ans = (char**)malloc(sizeof(char*));
    ans[0] = (char*)malloc(1);
    ans[0][0] = '\0';
    int ansSize = 1;

    for (int g = 0; g < groupCount; g++) {
        int newSize = ansSize * groupSizes[g];
        char** next = (char**)malloc((size_t)newSize * sizeof(char*));
        int idx = 0;
        for (int a = 0; a < ansSize; a++) {
            for (int c = 0; c < groupSizes[g]; c++) {
                int len = (int)strlen(ans[a]);
                next[idx] = (char*)malloc((size_t)len + 2);
                strcpy(next[idx], ans[a]);
                next[idx][len] = groups[g][c];
                next[idx][len + 1] = '\0';
                idx++;
            }
            free(ans[a]);
        }
        free(ans);
        ans = next;
        ansSize = newSize;
    }
    *returnSize = ansSize;
    return ans;
}
