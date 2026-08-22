// LeetCode 3009 - Maximum Number of Intersections on the Chart
// https://leetcode.com/problems/maximum-number-of-intersections-on-the-chart/

#include <stdlib.h>
#include <stdbool.h>

typedef struct { int key, val; bool used; } HEnt;
static unsigned hash_u(unsigned x) { x ^= x >> 16; x *= 0x7feb352dU; x ^= x >> 15; x *= 0x846ca68bU; x ^= x >> 16; return x; }
static void hadd(HEnt* t, int cap, int key, int d) {
    unsigned h = hash_u((unsigned)key) & (unsigned)(cap - 1);
    while (t[h].used) {
        if (t[h].key == key) { t[h].val += d; return; }
        h = (h + 1) & (unsigned)(cap - 1);
    }
    t[h].used = true; t[h].key = key; t[h].val = d;
}
static int cmp_int(const void* a, const void* b) { return (*(const int*)a) - (*(const int*)b); }

int maxIntersectionCount(int* y, int ySize) {
    int n = ySize;
    int cap = 1;
    while (cap < n * 4 + 16) cap <<= 1;
    HEnt* line = (HEnt*)calloc((size_t)cap, sizeof(HEnt));
    for (int i = 1; i < n; i++) {
        int start = 2 * y[i - 1], end = 2 * y[i];
        if (i != n - 1) {
            if (y[i] > y[i - 1]) end--;
            else end++;
        }
        int a = start, b = end;
        if (a > b) { int t = a; a = b; b = t; }
        hadd(line, cap, a, 1);
        hadd(line, cap, b + 1, -1);
    }
    int* keys = (int*)malloc((size_t)cap * sizeof(int));
    int kn = 0;
    for (int i = 0; i < cap; i++) if (line[i].used) keys[kn++] = line[i].key;
    qsort(keys, (size_t)kn, sizeof(int), cmp_int);
    int ans = 0, cur = 0;
    for (int i = 0; i < kn; i++) {
        unsigned h = hash_u((unsigned)keys[i]) & (unsigned)(cap - 1);
        while (line[h].used && line[h].key != keys[i]) h = (h + 1) & (unsigned)(cap - 1);
        cur += line[h].val;
        if (cur > ans) ans = cur;
    }
    free(line); free(keys);
    return ans;
}
