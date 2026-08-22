// LeetCode 2364 - Count Number of Bad Pairs
// https://leetcode.com/problems/count-number-of-bad-pairs/

#include <stdlib.h>
#include <stdbool.h>

typedef struct { int key; long long val; bool used; } Ent;

long long countBadPairs(int* nums, int numsSize) {
    long long n = numsSize;
    long long total = n * (n - 1) / 2;
    int cap = 1;
    while (cap < numsSize * 2) cap <<= 1;
    Ent* tab = (Ent*)calloc((size_t)cap, sizeof(Ent));
    long long good = 0;
    for (int i = 0; i < numsSize; i++) {
        int key = nums[i] - i;
        unsigned h = (unsigned)key * 2654435761u;
        int j = (int)(h & (unsigned)(cap - 1));
        while (tab[j].used && tab[j].key != key) j = (j + 1) & (cap - 1);
        if (tab[j].used) { good += tab[j].val; tab[j].val++; }
        else { tab[j].used = true; tab[j].key = key; tab[j].val = 1; }
    }
    free(tab);
    return total - good;
}
