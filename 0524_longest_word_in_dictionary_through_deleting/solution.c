// LeetCode 0524 - Longest Word in Dictionary through Deleting
// https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

static bool isSubsequence(const char* word, const char* source) {
    int index = 0;
    const int wordLength = (int)strlen(word);
    for (int sourceIndex = 0; source[sourceIndex] != '\0'; sourceIndex++) {
        if (index < wordLength && word[index] == source[sourceIndex]) {
            index++;
        }
    }
    return index == wordLength;
}

static bool isBetter(const char* candidate, const char* best) {
    const int candidateLength = (int)strlen(candidate);
    const int bestLength = (int)strlen(best);
    if (candidateLength > bestLength) {
        return true;
    }
    if (candidateLength < bestLength) {
        return false;
    }
    return strcmp(candidate, best) < 0;
}

char* findLongestWord(char* s, char** dictionary, int dictionarySize) {
    char* best = strdup("");
    for (int index = 0; index < dictionarySize; index++) {
        if (isSubsequence(dictionary[index], s) && isBetter(dictionary[index], best)) {
            free(best);
            best = strdup(dictionary[index]);
        }
    }
    return best;
}
