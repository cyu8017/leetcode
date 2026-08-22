// LeetCode 2788 - Split Strings by Separator
// https://leetcode.com/problems/split-strings-by-separator/

#include <stdlib.h>
#include <string.h>

char** splitWordsBySeparator(char** words, int wordsSize, char* separator, int* returnSize) {
    char sep = separator[0];
    int cap = 16, sz = 0;
    char** ans = (char**)malloc(cap * sizeof(char*));
    for (int w = 0; w < wordsSize; w++) {
        char* s = words[w];
        int start = 0, len = (int)strlen(s);
        for (int i = 0; i <= len; i++) {
            if (i == len || s[i] == sep) {
                if (i > start) {
                    if (sz == cap) { cap *= 2; ans = (char**)realloc(ans, cap * sizeof(char*)); }
                    int L = i - start;
                    ans[sz] = (char*)malloc(L + 1);
                    memcpy(ans[sz], s + start, L);
                    ans[sz][L] = 0;
                    sz++;
                }
                start = i + 1;
            }
        }
    }
    *returnSize = sz;
    return ans;
}
