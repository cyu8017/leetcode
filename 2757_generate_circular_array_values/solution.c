// LeetCode 2757 - Generate Circular Array Values
// https://leetcode.com/problems/generate-circular-array-values/

#include <stdlib.h>

typedef struct {
    int* arr;
    int n;
    int i;
} CyclicGenerator;

CyclicGenerator* cyclicGeneratorCreate(int* arr, int arrSize, int startIndex) {
    CyclicGenerator* g = (CyclicGenerator*)malloc(sizeof(CyclicGenerator));
    g->arr = arr;
    g->n = arrSize;
    g->i = startIndex;
    return g;
}

int cyclicGeneratorNext(CyclicGenerator* g) {
    int v = g->arr[g->i];
    g->i = (g->i + 1) % g->n;
    return v;
}

void cyclicGeneratorFree(CyclicGenerator* g) {
    free(g);
}
