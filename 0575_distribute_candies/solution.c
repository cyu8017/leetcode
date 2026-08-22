// LeetCode 0575 - Distribute Candies
// https://leetcode.com/problems/distribute-candies/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int distributeCandies(int* candyType, int candyTypeSize) {
    qsort(candyType, (size_t)candyTypeSize, sizeof(int), cmpInt);
    int unique = 0;
    for (int i = 0; i < candyTypeSize; i++) {
        if (i == 0 || candyType[i] != candyType[i - 1]) {
            unique++;
        }
    }
    int half = candyTypeSize / 2;
    return unique < half ? unique : half;
}
