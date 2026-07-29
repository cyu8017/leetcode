// LeetCode 1451 - Rearrange Words in a Sentence
// https://leetcode.com/problems/rearrange-words-in-a-sentence/

#include <stdlib.h>
#include <string.h>
#include <ctype.h>

static int cmp_len(const void* a, const void* b) {
    return (int)strlen(*(char**)a) - (int)strlen(*(char**)b);
}

char* arrangeWords(char* text) {
    int n = (int)strlen(text);
    char* copy = (char*)malloc(n + 1);
    for (int i = 0; i < n; i++) copy[i] = (char)tolower((unsigned char)text[i]);
    copy[n] = '\0';
    char** words = (char**)malloc(n * sizeof(char*));
    int wn = 0;
    for (char* tok = strtok(copy, " "); tok; tok = strtok(NULL, " ")) words[wn++] = tok;
    qsort(words, wn, sizeof(char*), cmp_len);
    char* ans = (char*)malloc(n + wn + 1);
    int idx = 0;
    for (int i = 0; i < wn; i++) {
        if (i) ans[idx++] = ' ';
        int L = (int)strlen(words[i]);
        memcpy(ans + idx, words[i], L);
        idx += L;
    }
    ans[idx] = '\0';
    if (idx) ans[0] = (char)toupper((unsigned char)ans[0]);
    free(copy); free(words);
    return ans;
}
