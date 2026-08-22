// LeetCode 2561 - Rearranging Fruits
// https://leetcode.com/problems/rearranging-fruits/

#include <stdlib.h>
#include <string.h>

typedef struct { int key; int val; } KV;

static int cmpKV(const void* a, const void* b) {
    return ((const KV*)a)->key - ((const KV*)b)->key;
}
static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

long long minCost(int* basket1, int basket1Size, int* basket2, int basket2Size) {
    KV* freq = (KV*)malloc((size_t)(basket1Size + basket2Size) * sizeof(KV));
    int fc = 0;
    int mn = 1 << 30;
    for (int i = 0; i < basket1Size; i++) {
        int x = basket1[i];
        if (x < mn) mn = x;
        int found = 0;
        for (int j = 0; j < fc; j++) if (freq[j].key == x) { freq[j].val++; found = 1; break; }
        if (!found) { freq[fc].key = x; freq[fc].val = 1; fc++; }
    }
    for (int i = 0; i < basket2Size; i++) {
        int x = basket2[i];
        if (x < mn) mn = x;
        int found = 0;
        for (int j = 0; j < fc; j++) if (freq[j].key == x) { freq[j].val--; found = 1; break; }
        if (!found) { freq[fc].key = x; freq[fc].val = -1; fc++; }
    }
    int* extra = (int*)malloc((size_t)(basket1Size + basket2Size) * sizeof(int));
    int ec = 0;
    for (int i = 0; i < fc; i++) {
        if (freq[i].val % 2 != 0) { free(freq); free(extra); return -1; }
        int c = freq[i].val;
        if (c < 0) c = -c;
        for (int j = 0; j < c / 2; j++) extra[ec++] = freq[i].key;
    }
    qsort(extra, (size_t)ec, sizeof(int), cmpInt);
    long long ans = 0;
    for (int i = 0; i < ec / 2; i++) {
        long long a = extra[i];
        long long b = 2LL * mn;
        ans += a < b ? a : b;
    }
    free(freq);
    free(extra);
    return ans;
}
