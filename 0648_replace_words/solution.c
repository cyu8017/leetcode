// LeetCode 0648 - Replace Words
// https://leetcode.com/problems/replace-words/

#define _POSIX_C_SOURCE 200809L
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* replaceWords(char** dictionary, int dictionarySize, char* sentence) {
    char* result = (char*)malloc(strlen(sentence) + 1);
    result[0] = '\0';
    char* copy = strdup(sentence);
    char* save = NULL;
    char* word = strtok_r(copy, " ", &save);
    int first = 1;
    while (word) {
        const char* replacement = word;
        int bestLen = (int)strlen(word) + 1;
        for (int i = 0; i < dictionarySize; i++) {
            int len = (int)strlen(dictionary[i]);
            if (len < bestLen && strncmp(word, dictionary[i], (size_t)len) == 0) {
                replacement = dictionary[i];
                bestLen = len;
            }
        }
        if (!first) {
            strcat(result, " ");
        }
        strcat(result, replacement);
        first = 0;
        word = strtok_r(NULL, " ", &save);
    }
    free(copy);
    return result;
}
