// LeetCode 0833 - Find And Replace in String
// https://leetcode.com/problems/find-and-replace-in-string/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

char* findReplaceString(char* s, int* indices, int indicesSize, char** sources, int sourcesSize, char** targets, int targetsSize) {
    (void)sourcesSize; (void)targetsSize;
    int n = (int)strlen(s);
    int* rlen = (int*)calloc((size_t)n, sizeof(int));
    char** rtgt = (char**)calloc((size_t)n, sizeof(char*));
    for (int k = 0; k < indicesSize; k++) {
        int i = indices[k];
        int slen = (int)strlen(sources[k]);
        if (i + slen <= n && strncmp(s + i, sources[k], (size_t)slen) == 0) {
            rlen[i] = slen;
            rtgt[i] = targets[k];
        }
    }
    char* ans = (char*)malloc((size_t)n * 20 + 1);
    int pos = 0, i = 0;
    while (i < n) {
        if (rlen[i]) {
            int tlen = (int)strlen(rtgt[i]);
            memcpy(ans + pos, rtgt[i], (size_t)tlen);
            pos += tlen;
            i += rlen[i];
        } else {
            ans[pos++] = s[i++];
        }
    }
    ans[pos] = '\0';
    free(rlen); free(rtgt);
    return ans;
}
