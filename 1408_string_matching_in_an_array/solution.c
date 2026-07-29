// LeetCode 1408 - String Matching in an Array
// https://leetcode.com/problems/string-matching-in-an-array/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

char** stringMatching(char** words, int wordsSize, int* returnSize) {
    char** ans = (char**)malloc(wordsSize * sizeof(char*));
    int an = 0;
    for (int i = 0; i < wordsSize; i++) {
        bool ok = false;
        for (int j = 0; j < wordsSize; j++) {
            if (i != j && strstr(words[j], words[i])) { ok = true; break; }
        }
        if (ok) {
            ans[an] = (char*)malloc(strlen(words[i]) + 1);
            strcpy(ans[an], words[i]);
            an++;
        }
    }
    *returnSize = an;
    return ans;
}
