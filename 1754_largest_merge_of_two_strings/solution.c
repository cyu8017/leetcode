// LeetCode 1754 - Largest Merge Of Two Strings
// https://leetcode.com/problems/largest-merge-of-two-strings/

#include <stdlib.h>
#include <string.h>

char* largestMerge(char* word1, char* word2) {
    size_t len1 = strlen(word1);
    size_t len2 = strlen(word2);
    char* out = (char*) malloc(len1 + len2 + 1);
    size_t i = 0;
    size_t j = 0;
    size_t pos = 0;
    while (i < len1 && j < len2) {
        if (strcmp(word1 + i, word2 + j) > 0) {
            out[pos++] = word1[i++];
        } else {
            out[pos++] = word2[j++];
        }
    }
    while (i < len1) {
        out[pos++] = word1[i++];
    }
    while (j < len2) {
        out[pos++] = word2[j++];
    }
    out[pos] = '\0';
    return out;
}
