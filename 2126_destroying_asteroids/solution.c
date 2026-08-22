// LeetCode 2126 - Destroying Asteroids
// https://leetcode.com/problems/destroying-asteroids/

#include <stdlib.h>
#include <stdbool.h>

static int cmpInt(const void* a, const void* b) {
    int x = *(const int*)a, y = *(const int*)b;
    return (x > y) - (x < y);
}

bool asteroidsDestroyed(int mass, int* asteroids, int asteroidsSize) {
    qsort(asteroids, (size_t)asteroidsSize, sizeof(int), cmpInt);
    long long cur = mass;
    for (int i = 0; i < asteroidsSize; i++) {
        if (cur < asteroids[i]) return false;
        cur += asteroids[i];
    }
    return true;
}
