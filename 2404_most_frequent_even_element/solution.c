// LeetCode 2404 - Most Frequent Even Element
// https://leetcode.com/problems/most-frequent-even-element/

#include <stdlib.h>
#include <stdbool.h>

int mostFrequentEven(int* nums, int numsSize) {
    int cap = 1024;
    typedef struct { int key, val; bool used; } E;
    E* tab = (E*)calloc((size_t)cap, sizeof(E));
    int ans = -1, best = 0;
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i];
        if (x % 2 != 0) continue;
        unsigned h = (unsigned)x * 2654435761u;
        int j = (int)(h & (unsigned)(cap - 1));
        while (tab[j].used && tab[j].key != x) j = (j + 1) & (cap - 1);
        if (!tab[j].used) { tab[j].used = true; tab[j].key = x; tab[j].val = 0; }
        tab[j].val++;
        if (tab[j].val > best || (tab[j].val == best && (ans == -1 || x < ans))) {
            best = tab[j].val; ans = x;
        }
    }
    free(tab);
    return ans;
}
