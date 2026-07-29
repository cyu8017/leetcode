// LeetCode 0737 - Sentence Similarity II
// https://leetcode.com/problems/sentence-similarity-ii/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char** words;
    int* parent;
    int size;
    int capacity;
} UF;

static int ufFindWord(UF* uf, const char* word) {
    for (int i = 0; i < uf->size; i++) {
        if (strcmp(uf->words[i], word) == 0) {
            return i;
        }
    }
    return -1;
}

static int ufAdd(UF* uf, const char* word) {
    int idx = ufFindWord(uf, word);
    if (idx >= 0) return idx;
    if (uf->size == uf->capacity) {
        uf->capacity = uf->capacity ? uf->capacity * 2 : 16;
        uf->words = (char**)realloc(uf->words, (size_t)uf->capacity * sizeof(char*));
        uf->parent = (int*)realloc(uf->parent, (size_t)uf->capacity * sizeof(int));
    }
    uf->words[uf->size] = (char*)word;
    uf->parent[uf->size] = uf->size;
    return uf->size++;
}

static int ufFind(UF* uf, int x) {
    while (uf->parent[x] != x) {
        uf->parent[x] = uf->parent[uf->parent[x]];
        x = uf->parent[x];
    }
    return x;
}

static void ufUnion(UF* uf, int a, int b) {
    uf->parent[ufFind(uf, a)] = ufFind(uf, b);
}

bool areSentencesSimilarTwo(char** sentence1, int sentence1Size, char** sentence2, int sentence2Size, char*** similarPairs, int similarPairsSize, int* similarPairsColSize) {
    (void)similarPairsColSize;
    if (sentence1Size != sentence2Size) {
        return false;
    }
    UF uf = {0};
    for (int i = 0; i < similarPairsSize; i++) {
        int a = ufAdd(&uf, similarPairs[i][0]);
        int b = ufAdd(&uf, similarPairs[i][1]);
        ufUnion(&uf, a, b);
    }
    for (int i = 0; i < sentence1Size; i++) {
        int a = ufAdd(&uf, sentence1[i]);
        int b = ufAdd(&uf, sentence2[i]);
        if (ufFind(&uf, a) != ufFind(&uf, b)) {
            free(uf.words);
            free(uf.parent);
            return false;
        }
    }
    free(uf.words);
    free(uf.parent);
    return true;
}
