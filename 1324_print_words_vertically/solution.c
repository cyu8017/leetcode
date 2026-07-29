// LeetCode 1324 - Print Words Vertically
// https://leetcode.com/problems/print-words-vertically/

#include <stdlib.h>
#include <string.h>

char** printVertically(char* s, int* returnSize) {
    char* words[200];
    int wcount = 0, maxLen = 0;
    char* copy = (char*)malloc(strlen(s) + 1);
    strcpy(copy, s);
    for (char* tok = strtok(copy, " "); tok; tok = strtok(NULL, " ")) {
        words[wcount++] = tok;
        int L = (int)strlen(tok);
        if (L > maxLen) maxLen = L;
    }
    char** ans = (char**)malloc(maxLen * sizeof(char*));
    for (int i = 0; i < maxLen; i++) {
        char* row = (char*)malloc(wcount + 1);
        int len = 0;
        for (int w = 0; w < wcount; w++) {
            int L = (int)strlen(words[w]);
            row[len++] = i < L ? words[w][i] : ' ';
        }
        while (len > 0 && row[len - 1] == ' ') len--;
        row[len] = '\0';
        ans[i] = row;
    }
    free(copy);
    *returnSize = maxLen;
    return ans;
}
