// LeetCode 1996 - The Number of Weak Characters in the Game
// https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/

#include <stdlib.h>

static int cmpProp(const void* a, const void* b) {
    int* const* x = (int* const*)a;
    int* const* y = (int* const*)b;
    if ((*x)[0] != (*y)[0]) return (*y)[0] - (*x)[0];
    return (*x)[1] - (*y)[1];
}

int numberOfWeakCharacters(int** properties, int propertiesSize, int* propertiesColSize) {
    (void)propertiesColSize;
    qsort(properties, (size_t)propertiesSize, sizeof(int*), cmpProp);
    int maxDef = 0, ans = 0;
    for (int i = 0; i < propertiesSize; i++) {
        if (properties[i][1] < maxDef) ans++;
        else maxDef = properties[i][1];
    }
    return ans;
}
