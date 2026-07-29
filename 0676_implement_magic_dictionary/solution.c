// LeetCode 0676 - Implement Magic Dictionary
// https://leetcode.com/problems/implement-magic-dictionary/

#define _POSIX_C_SOURCE 200809L
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char** words;
    int size;
} MagicDictionary;

MagicDictionary* magicDictionaryCreate() {
    MagicDictionary* obj = (MagicDictionary*)malloc(sizeof(MagicDictionary));
    obj->words = NULL;
    obj->size = 0;
    return obj;
}

void magicDictionaryBuildDict(MagicDictionary* obj, char** dictionary, int dictionarySize) {
    obj->size = dictionarySize;
    obj->words = (char**)malloc((size_t)dictionarySize * sizeof(char*));
    for (int i = 0; i < dictionarySize; i++) obj->words[i] = strdup(dictionary[i]);
}

bool magicDictionarySearch(MagicDictionary* obj, char* searchWord) {
    int n = (int)strlen(searchWord);
    for (int i = 0; i < obj->size; i++) {
        if ((int)strlen(obj->words[i]) != n) continue;
        int diff = 0;
        for (int j = 0; j < n; j++) if (obj->words[i][j] != searchWord[j] && ++diff > 1) break;
        if (diff == 1) return true;
    }
    return false;
}

void magicDictionaryFree(MagicDictionary* obj) {
    for (int i = 0; i < obj->size; i++) free(obj->words[i]);
    free(obj->words);
    free(obj);
}
