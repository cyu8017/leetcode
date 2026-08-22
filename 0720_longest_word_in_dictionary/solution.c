// LeetCode 0720 - Longest Word in Dictionary
// https://leetcode.com/problems/longest-word-in-dictionary/

#include <stdlib.h>
#include <string.h>

static int cmpStr(const void* a, const void* b) {
    return strcmp(*(char* const*)a, *(char* const*)b);
}

char* longestWord(char** words, int wordsSize) {
    qsort(words, (size_t)wordsSize, sizeof(char*), cmpStr);
    char** built = (char**)malloc((size_t)(wordsSize + 1) * sizeof(char*));
    int builtSize = 0;
    built[builtSize++] = "";
    char* best = "";
    for (int i = 0; i < wordsSize; i++) {
        char* word = words[i];
        int len = (int)strlen(word);
        char* prefix = (char*)malloc((size_t)len);
        memcpy(prefix, word, (size_t)(len - 1));
        prefix[len - 1] = '\0';
        int ok = 0;
        for (int j = 0; j < builtSize; j++) {
            if (strcmp(built[j], prefix) == 0) {
                ok = 1;
                break;
            }
        }
        free(prefix);
        if (ok) {
            built[builtSize++] = word;
            if (len > (int)strlen(best)) {
                best = word;
            }
        }
    }
    free(built);
    char* out = (char*)malloc(strlen(best) + 1);
    strcpy(out, best);
    return out;
}
