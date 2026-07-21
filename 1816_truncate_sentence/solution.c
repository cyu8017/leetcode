// LeetCode 1816 - Truncate Sentence
// https://leetcode.com/problems/truncate-sentence/

#include <stdlib.h>
#include <string.h>

char* truncateSentence(char* s, int k) {
    int n = (int)strlen(s);
    int words = 0;
    int end = n;
    for (int i = 0; i < n; i++) {
        if (s[i] == ' ') {
            words++;
            if (words == k) {
                end = i;
                break;
            }
        }
    }
    char* result = (char*)malloc((size_t)end + 1);
    memcpy(result, s, (size_t)end);
    result[end] = '\0';
    return result;
}
