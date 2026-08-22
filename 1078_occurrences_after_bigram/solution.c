// LeetCode 1078 - Occurrences After Bigram
// https://leetcode.com/problems/occurrences-after-bigram/

#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** findOcurrences(char* text, char* first, char* second, int* returnSize) {
    char* copy = (char*)malloc(strlen(text) + 1);
    strcpy(copy, text);
    char* words[1001];
    int wordCount = 0;
    char* tok = strtok(copy, " ");
    while (tok) {
        words[wordCount++] = tok;
        tok = strtok(NULL, " ");
    }
    int cap = 16;
    char** ans = (char**)malloc((size_t)cap * sizeof(char*));
    int count = 0;
    for (int i = 0; i + 2 < wordCount; i++) {
        if (strcmp(words[i], first) == 0 && strcmp(words[i + 1], second) == 0) {
            if (count == cap) {
                cap *= 2;
                ans = (char**)realloc(ans, (size_t)cap * sizeof(char*));
            }
            ans[count] = (char*)malloc(strlen(words[i + 2]) + 1);
            strcpy(ans[count], words[i + 2]);
            count++;
        }
    }
    free(copy);
    *returnSize = count;
    return ans;
}
