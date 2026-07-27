// LeetCode 1054 - Distant Barcodes
// https://leetcode.com/problems/distant-barcodes/

#include <stdlib.h>
#include <string.h>

typedef struct {
    int value;
    int freq;
} Pair;

static int cmpPair(const void* a, const void* b) {
    const Pair* pa = (const Pair*)a;
    const Pair* pb = (const Pair*)b;
    if (pb->freq != pa->freq) {
        return pb->freq - pa->freq;
    }
    return pa->value - pb->value;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* rearrangeBarcodes(int* barcodes, int barcodesSize, int* returnSize) {
    int* freq = (int*)calloc(10001, sizeof(int));
    for (int i = 0; i < barcodesSize; i++) {
        freq[barcodes[i]]++;
    }
    Pair* pairs = (Pair*)malloc(10001 * sizeof(Pair));
    int pairCount = 0;
    for (int v = 1; v <= 10000; v++) {
        if (freq[v]) {
            pairs[pairCount].value = v;
            pairs[pairCount].freq = freq[v];
            pairCount++;
        }
    }
    qsort(pairs, (size_t)pairCount, sizeof(Pair), cmpPair);
    int* ans = (int*)calloc((size_t)barcodesSize, sizeof(int));
    int idx = 0;
    for (int p = 0; p < pairCount; p++) {
        for (int k = 0; k < pairs[p].freq; k++) {
            ans[idx] = pairs[p].value;
            idx += 2;
            if (idx >= barcodesSize) {
                idx = 1;
            }
        }
    }
    free(freq);
    free(pairs);
    *returnSize = barcodesSize;
    return ans;
}
