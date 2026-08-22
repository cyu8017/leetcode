// LeetCode 2107 - Number of Unique Flavors After Sharing K Candies
// https://leetcode.com/problems/number-of-unique-flavors-after-sharing-k-candies/

#include <stdlib.h>

typedef struct { int key, cnt; int used; } MapE2107;

static unsigned h2107(int k) { return (unsigned)k * 2654435761u; }

static int* mapRef2107(MapE2107* tab, int cap, int key, int create) {
    int idx = (int)(h2107(key) & (unsigned)(cap - 1));
    for (;;) {
        if (!tab[idx].used) {
            if (!create) return NULL;
            tab[idx].used = 1; tab[idx].key = key; tab[idx].cnt = 0;
            return &tab[idx].cnt;
        }
        if (tab[idx].key == key) return &tab[idx].cnt;
        idx = (idx + 1) & (cap - 1);
    }
}

static int mapSize2107(MapE2107* tab, int cap) {
    int s = 0;
    for (int i = 0; i < cap; i++) if (tab[i].used && tab[i].cnt > 0) s++;
    return s;
}

int shareCandies(int* candies, int candiesSize, int k) {
    int n = candiesSize;
    int cap = 1;
    while (cap < n * 4 + 16) cap *= 2;
    MapE2107* freq = (MapE2107*)calloc((size_t)cap, sizeof(MapE2107));
    for (int i = 0; i < n; i++) (*mapRef2107(freq, cap, candies[i], 1))++;
    if (k == 0) {
        int ans = mapSize2107(freq, cap);
        free(freq);
        return ans;
    }
    for (int i = 0; i < k; i++) {
        int* p = mapRef2107(freq, cap, candies[i], 1);
        (*p)--;
    }
    int ans = mapSize2107(freq, cap);
    for (int i = k; i < n; i++) {
        (*mapRef2107(freq, cap, candies[i - k], 1))++;
        (*mapRef2107(freq, cap, candies[i], 1))--;
        int cur = mapSize2107(freq, cap);
        if (cur > ans) ans = cur;
    }
    free(freq);
    return ans;
}
