// LeetCode 2352 - Equal Row and Column Pairs
// https://leetcode.com/problems/equal-row-and-column-pairs/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct { char* key; int val; bool used; } Ent;

static unsigned hashBytes(const char* s, int n) {
    unsigned h = 2166136261u;
    for (int i = 0; i < n; i++) { h ^= (unsigned char)s[i]; h *= 16777619u; }
    return h;
}

int equalPairs(int** grid, int gridSize, int* gridColSize) {
    (void)gridColSize;
    int n = gridSize;
    int keyLen = n * 4;
    int cap = 1;
    while (cap < n * 4) cap <<= 1;
    Ent* tab = (Ent*)calloc((size_t)cap, sizeof(Ent));
    char* buf = (char*)malloc((size_t)keyLen);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int v = grid[i][j];
            buf[j*4] = (char)(v >> 24); buf[j*4+1] = (char)(v >> 16);
            buf[j*4+2] = (char)(v >> 8); buf[j*4+3] = (char)v;
        }
        unsigned h = hashBytes(buf, keyLen);
        int idx = (int)(h & (unsigned)(cap - 1));
        while (tab[idx].used) {
            if (memcmp(tab[idx].key, buf, (size_t)keyLen) == 0) { tab[idx].val++; break; }
            idx = (idx + 1) & (cap - 1);
        }
        if (!tab[idx].used) {
            tab[idx].used = true;
            tab[idx].key = (char*)malloc((size_t)keyLen);
            memcpy(tab[idx].key, buf, (size_t)keyLen);
            tab[idx].val = 1;
        }
    }
    int ans = 0;
    for (int j = 0; j < n; j++) {
        for (int i = 0; i < n; i++) {
            int v = grid[i][j];
            buf[i*4] = (char)(v >> 24); buf[i*4+1] = (char)(v >> 16);
            buf[i*4+2] = (char)(v >> 8); buf[i*4+3] = (char)v;
        }
        unsigned h = hashBytes(buf, keyLen);
        int idx = (int)(h & (unsigned)(cap - 1));
        while (tab[idx].used) {
            if (memcmp(tab[idx].key, buf, (size_t)keyLen) == 0) { ans += tab[idx].val; break; }
            idx = (idx + 1) & (cap - 1);
        }
    }
    for (int i = 0; i < cap; i++) if (tab[i].used) free(tab[i].key);
    free(tab); free(buf);
    return ans;
}
