// LeetCode 1286 - Iterator for Combination
// https://leetcode.com/problems/iterator-for-combination/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char* characters;
    int n;
    int k;
    int* idx;
    char* current;
    bool hasNextItem;
} CombinationIterator;

static void build_combo(CombinationIterator* obj) {
    for (int i = 0; i < obj->k; i++) obj->current[i] = obj->characters[obj->idx[i]];
    obj->current[obj->k] = '\0';
}

static bool advance(CombinationIterator* obj) {
    for (int pos = obj->k - 1; pos >= 0; pos--) {
        obj->idx[pos]++;
        int limit = obj->n - obj->k + pos;
        if (obj->idx[pos] <= limit) {
            for (int j = pos + 1; j < obj->k; j++) obj->idx[j] = obj->idx[j - 1] + 1;
            build_combo(obj);
            return true;
        }
    }
    return false;
}

CombinationIterator* combinationIteratorCreate(char* characters, int combinationLength) {
    CombinationIterator* obj = (CombinationIterator*)malloc(sizeof(CombinationIterator));
    obj->n = (int)strlen(characters);
    obj->k = combinationLength;
    obj->characters = characters;
    obj->idx = (int*)malloc((size_t)combinationLength * sizeof(int));
    obj->current = (char*)malloc((size_t)combinationLength + 1);
    for (int i = 0; i < combinationLength; i++) obj->idx[i] = i;
    obj->hasNextItem = combinationLength <= obj->n;
    if (obj->hasNextItem) build_combo(obj);
    return obj;
}

char* combinationIteratorNext(CombinationIterator* obj) {
    char* ans = (char*)malloc((size_t)obj->k + 1);
    strcpy(ans, obj->current);
    obj->hasNextItem = advance(obj);
    return ans;
}

bool combinationIteratorHasNext(CombinationIterator* obj) {
    return obj->hasNextItem;
}

void combinationIteratorFree(CombinationIterator* obj) {
    if (!obj) return;
    free(obj->idx);
    free(obj->current);
    free(obj);
}
