// LeetCode 2418 - Sort the People
// https://leetcode.com/problems/sort-the-people/

#include <stdlib.h>

typedef struct { int h; int i; } P;
static int cmpP(const void* a, const void* b) { return ((const P*)b)->h - ((const P*)a)->h; }

char** sortPeople(char** names, int namesSize, int* heights, int heightsSize, int* returnSize) {
    (void)heightsSize;
    P* arr = (P*)malloc((size_t)namesSize * sizeof(P));
    for (int i = 0; i < namesSize; i++) arr[i] = (P){heights[i], i};
    qsort(arr, (size_t)namesSize, sizeof(P), cmpP);
    char** ans = (char**)malloc((size_t)namesSize * sizeof(char*));
    for (int i = 0; i < namesSize; i++) ans[i] = names[arr[i].i];
    free(arr);
    *returnSize = namesSize;
    return ans;
}
