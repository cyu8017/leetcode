// LeetCode 3074 - Apple Redistribution into Boxes
// https://leetcode.com/problems/apple-redistribution-into-boxes/

#include <stdlib.h>

static int cmp_int(const void* a, const void* b) {
    return (*(const int*)a) - (*(const int*)b);
}

int minimumBoxes(int* apple, int appleSize, int* capacity, int capacitySize) {
    qsort(capacity, (size_t)capacitySize, sizeof(int), cmp_int);
    int s = 0;
    for (int i = 0; i < appleSize; i++) s += apple[i];
    for (int i = 1; ; i++) {
        s -= capacity[capacitySize - i];
        if (s <= 0) return i;
    }
}
