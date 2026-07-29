// LeetCode 0890 - Find and Replace Pattern
// https://leetcode.com/problems/find-and-replace-pattern/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

static void normalize(const char* s, int* out) {
    int map[128];
    for (int i = 0; i < 128; i++) map[i] = -1;
    int next = 0;
    for (int i = 0; s[i]; i++) {
        unsigned char ch = (unsigned char)s[i];
        if (map[ch] < 0) map[ch] = next++;
        out[i] = map[ch];
    }
}

char** findAndReplacePattern(char** words, int wordsSize, char* pattern, int* returnSize) {
    int plen = (int)strlen(pattern);
    int* target = (int*)malloc((size_t)plen * sizeof(int));
    normalize(pattern, target);
    char** ans = (char**)malloc((size_t)wordsSize * sizeof(char*));
    int* tmp = (int*)malloc((size_t)plen * sizeof(int));
    int count = 0;
    for (int i = 0; i < wordsSize; i++) {
        if ((int)strlen(words[i]) != plen) continue;
        normalize(words[i], tmp);
        bool ok = true;
        for (int j = 0; j < plen; j++) if (tmp[j] != target[j]) { ok = false; break; }
        if (ok) ans[count++] = words[i];
    }
    free(target); free(tmp);
    *returnSize = count;
    return ans;
}
