// LeetCode 1859 - Sorting the Sentence
// https://leetcode.com/problems/sorting-the-sentence/

#include <ctype.h>
#include <stdlib.h>
#include <string.h>

char* sortSentence(char* s) {
    char* copy = (char*)malloc(strlen(s) + 1);
    strcpy(copy, s);
    char* tokens[9];
    int count = 0;
    char* tok = strtok(copy, " ");
    while (tok) {
        tokens[count++] = tok;
        tok = strtok(NULL, " ");
    }
    char* ordered[9];
    int lengths[9];
    for (int i = 0; i < count; i++) {
        int len = (int)strlen(tokens[i]);
        int pos = tokens[i][len - 1] - '1';
        ordered[pos] = tokens[i];
        lengths[pos] = len - 1;
    }
    int total = 0;
    for (int i = 0; i < count; i++) total += lengths[i] + (i ? 1 : 0);
    char* result = (char*)malloc((size_t)total + 1);
    int pos = 0;
    for (int i = 0; i < count; i++) {
        if (i) result[pos++] = ' ';
        memcpy(result + pos, ordered[i], (size_t)lengths[i]);
        pos += lengths[i];
    }
    result[pos] = '\0';
    free(copy);
    return result;
}
