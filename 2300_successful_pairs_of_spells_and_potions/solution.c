// LeetCode 2300 - Successful Pairs of Spells and Potions
// https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

#include <stdlib.h>

static int cmp_int(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int* successfulPairs(int* spells, int spellsSize, int* potions, int potionsSize, long long success, int* returnSize) {
    qsort(potions, (size_t)potionsSize, sizeof(int), cmp_int);
    int* ans = (int*)malloc((size_t)spellsSize * sizeof(int));
    for (int i = 0; i < spellsSize; i++) {
        int lo = 0, hi = potionsSize;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if ((long long)spells[i] * potions[mid] >= success) hi = mid;
            else lo = mid + 1;
        }
        ans[i] = potionsSize - lo;
    }
    *returnSize = spellsSize;
    return ans;
}
