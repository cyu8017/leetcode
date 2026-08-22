// LeetCode 1813 - Sentence Similarity III
// https://leetcode.com/problems/sentence-similarity-iii/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

static int splitWords(char* sentence, char*** out) {
    int capacity = 8, count = 0;
    char** words = (char**)malloc((size_t)capacity * sizeof(char*));
    char* copy = (char*)malloc(strlen(sentence) + 1);
    strcpy(copy, sentence);
    char* token = strtok(copy, " ");
    while (token) {
        if (count == capacity) {
            capacity *= 2;
            words = (char**)realloc(words, (size_t)capacity * sizeof(char*));
        }
        words[count] = (char*)malloc(strlen(token) + 1);
        strcpy(words[count], token);
        count++;
        token = strtok(NULL, " ");
    }
    free(copy);
    *out = words;
    return count;
}

static void freeWords(char** words, int n) {
    for (int i = 0; i < n; i++) free(words[i]);
    free(words);
}

bool areSentencesSimilar(char* sentence1, char* sentence2) {
    char **words1 = NULL, **words2 = NULL;
    int n1 = splitWords(sentence1, &words1);
    int n2 = splitWords(sentence2, &words2);

    int i = 0;
    while (i < n1 && i < n2 && strcmp(words1[i], words2[i]) == 0) i++;
    if (i == n1 || i == n2) {
        freeWords(words1, n1);
        freeWords(words2, n2);
        return true;
    }

    int j1 = n1 - 1, j2 = n2 - 1;
    while (j1 >= i && j2 >= i && strcmp(words1[j1], words2[j2]) == 0) {
        j1--;
        j2--;
    }
    bool ok = j1 < i || j2 < i;
    freeWords(words1, n1);
    freeWords(words2, n2);
    return ok;
}
