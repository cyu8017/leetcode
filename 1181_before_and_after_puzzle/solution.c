// LeetCode 1181 - Before and After Puzzle
// https://leetcode.com/problems/before-and-after-puzzle/

#include <stdlib.h>
#include <string.h>

static int cmpStr(const void* a, const void* b) {
    return strcmp(*(const char* const*)a, *(const char* const*)b);
}

static int splitWords(char* phrase, char** words, int maxWords) {
    int count = 0;
    char* token = strtok(phrase, " ");
    while (token && count < maxWords) {
        words[count++] = token;
        token = strtok(NULL, " ");
    }
    return count;
}

static char* joinPhrases(char** first, int firstSize, char** second, int secondSize) {
    int len = 0;
    for (int i = 0; i < firstSize; i++) len += (int)strlen(first[i]) + 1;
    for (int i = 1; i < secondSize; i++) len += (int)strlen(second[i]) + 1;
    char* out = (char*)malloc((size_t)len + 1);
    out[0] = '\0';
    for (int i = 0; i < firstSize; i++) {
        if (i > 0) strcat(out, " ");
        strcat(out, first[i]);
    }
    for (int i = 1; i < secondSize; i++) {
        strcat(out, " ");
        strcat(out, second[i]);
    }
    return out;
}

char** beforeAndAfterPuzzles(char** phrases, int phrasesSize, int* returnSize) {
    char*** split = (char***)malloc((size_t)phrasesSize * sizeof(char**));
    int* sizes = (int*)malloc((size_t)phrasesSize * sizeof(int));
    char** copies = (char**)malloc((size_t)phrasesSize * sizeof(char*));
    for (int i = 0; i < phrasesSize; i++) {
        copies[i] = strdup(phrases[i]);
        split[i] = (char**)malloc(64 * sizeof(char*));
        sizes[i] = splitWords(copies[i], split[i], 64);
    }
    char** uniq = (char**)malloc((size_t)phrasesSize * phrasesSize * sizeof(char*));
    int uniqCount = 0;
    for (int i = 0; i < phrasesSize; i++) {
        for (int j = 0; j < phrasesSize; j++) {
            if (i == j) continue;
            if (strcmp(split[i][sizes[i] - 1], split[j][0]) != 0) continue;
            char* combined = joinPhrases(split[i], sizes[i], split[j], sizes[j]);
            int found = 0;
            for (int k = 0; k < uniqCount; k++) {
                if (strcmp(uniq[k], combined) == 0) {
                    found = 1;
                    break;
                }
            }
            if (!found) uniq[uniqCount++] = combined;
            else free(combined);
        }
    }
    qsort(uniq, (size_t)uniqCount, sizeof(char*), cmpStr);
    for (int i = 0; i < phrasesSize; i++) {
        free(split[i]);
        free(copies[i]);
    }
    free(split);
    free(sizes);
    free(copies);
    *returnSize = uniqCount;
    return uniq;
}
