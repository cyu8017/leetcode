// LeetCode 1196 - How Many Apples Can You Put into the Basket
// https://leetcode.com/problems/how-many-apples-can-you-put-into-the-basket/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int maxNumberOfApples(int* weight, int weightSize) {
    qsort(weight, (size_t)weightSize, sizeof(int), cmpInt);
    int total = 0;
    for (int i = 0; i < weightSize; i++) {
        total += weight[i];
        if (total > 5000) return i;
    }
    return weightSize;
}
