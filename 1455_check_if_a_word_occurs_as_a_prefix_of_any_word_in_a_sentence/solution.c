// LeetCode 1455 - Check If a Word Occurs As a Prefix of Any Word in a Sentence
// https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/

#include <string.h>
#include <stdlib.h>

int isPrefixOfWord(char* sentence, char* searchWord) {
    char* copy = (char*)malloc(strlen(sentence) + 1);
    strcpy(copy, sentence);
    int i = 1;
    for (char* tok = strtok(copy, " "); tok; tok = strtok(NULL, " "), i++) {
        if (strncmp(tok, searchWord, strlen(searchWord)) == 0) {
            free(copy);
            return i;
        }
    }
    free(copy);
    return -1;
}
