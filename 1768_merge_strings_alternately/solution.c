// LeetCode 1768 - Merge Strings Alternately
// https://leetcode.com/problems/merge-strings-alternately/

#include <stdlib.h>
#include <string.h>

char* mergeAlternately(char* word1, char* word2) {
    int len1 = (int)strlen(word1);
    int len2 = (int)strlen(word2);
    char* out = (char*)malloc((size_t)(len1 + len2 + 1));
    int i = 0, j = 0, k = 0;
    while (i < len1 || j < len2) {
        if (i < len1) {
            out[k++] = word1[i++];
        }
        if (j < len2) {
            out[k++] = word2[j++];
        }
    }
    out[k] = '\0';
    return out;
}
