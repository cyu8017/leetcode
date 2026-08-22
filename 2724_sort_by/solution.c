// LeetCode 2724 - Sort By
// https://leetcode.com/problems/sort-by/

#include <stdlib.h>

typedef double (*SortKeyFn)(void* item);

typedef struct { void* item; double key; } Pair2724;
static int cmp2724(const void* a, const void* b) {
    double da = ((const Pair2724*)a)->key, db = ((const Pair2724*)b)->key;
    return (da > db) - (da < db);
}

void** sortBy(void** arr, int arrSize, SortKeyFn fn, int* returnSize) {
    Pair2724* p = (Pair2724*)malloc((size_t)arrSize * sizeof(Pair2724));
    for (int i = 0; i < arrSize; i++) {
        p[i].item = arr[i];
        p[i].key = fn ? fn(arr[i]) : 0;
    }
    qsort(p, (size_t)arrSize, sizeof(Pair2724), cmp2724);
    void** out = (void**)malloc((size_t)arrSize * sizeof(void*));
    for (int i = 0; i < arrSize; i++) out[i] = p[i].item;
    free(p);
    *returnSize = arrSize;
    return out;
}
