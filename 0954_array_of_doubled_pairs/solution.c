// LeetCode 0954 - Array of Doubled Pairs
// https://leetcode.com/problems/array-of-doubled-pairs/

#include <stdbool.h>
#include <stdlib.h>

static int cmpAbs(const void* a, const void* b) {
    int x = *(const int*)a, y = *(const int*)b;
    int ax = x < 0 ? -x : x, ay = y < 0 ? -y : y;
    return ax - ay;
}

bool canReorderDoubled(int* arr, int arrSize) {
    // count via sort + scan on unique keys
    int* keys = (int*)malloc((size_t)arrSize * sizeof(int));
    for (int i = 0; i < arrSize; i++) keys[i] = arr[i];
    qsort(keys, (size_t)arrSize, sizeof(int), cmpAbs);
    // hash map open addressing for values -100000..100000 -> use offset
    #define OFF 100000
    int* count = (int*)calloc(200001, sizeof(int));
    for (int i = 0; i < arrSize; i++) count[arr[i] + OFF]++;
    for (int i = 0; i < arrSize; ) {
        int x = keys[i];
        while (i < arrSize && keys[i] == x) i++;
        int c = count[x + OFF];
        if (!c) continue;
        long long tw = (long long)x * 2;
        if (tw < -OFF || tw > OFF || count[tw + OFF] < c) {
            free(keys); free(count); return false;
        }
        count[tw + OFF] -= c;
        count[x + OFF] = 0;
    }
    free(keys); free(count);
    return true;
}
