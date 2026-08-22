// LeetCode 2975 - Maximum Square Area by Removing Fences From a Field
// https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/

#include <stdlib.h>
#include <stdbool.h>

static int cmp2975(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

typedef struct {
    int key;
    int used;
} HS2975;

static unsigned hash2975(int key) {
    unsigned x = (unsigned)key;
    x ^= x >> 16;
    x *= 0x7feb352dU;
    x ^= x >> 15;
    x *= 0x846ca68bU;
    x ^= x >> 16;
    return x;
}

static void hsAdd2975(HS2975* t, int cap, int key) {
    unsigned i = hash2975(key) & (unsigned)(cap - 1);
    while (t[i].used) {
        if (t[i].key == key) return;
        i = (i + 1) & (unsigned)(cap - 1);
    }
    t[i].used = 1;
    t[i].key = key;
}

static bool hsHas2975(HS2975* t, int cap, int key) {
    unsigned i = hash2975(key) & (unsigned)(cap - 1);
    while (t[i].used) {
        if (t[i].key == key) return true;
        i = (i + 1) & (unsigned)(cap - 1);
    }
    return false;
}

static HS2975* gaps2975(int* fences, int fencesSize, int bound, int* outCap, int** outKeys, int* outKeyCount) {
    int* arr = (int*)malloc((size_t)(fencesSize + 2) * sizeof(int));
    arr[0] = 1;
    for (int i = 0; i < fencesSize; i++) arr[i + 1] = fences[i];
    arr[fencesSize + 1] = bound;
    qsort(arr, (size_t)(fencesSize + 2), sizeof(int), cmp2975);
    int m = fencesSize + 2;
    int maxGaps = m * (m - 1) / 2 + 8;
    int cap = 1;
    while (cap < maxGaps * 2 + 16) cap <<= 1;
    HS2975* hs = (HS2975*)calloc((size_t)cap, sizeof(HS2975));
    int* keys = (int*)malloc((size_t)maxGaps * sizeof(int));
    int kc = 0;
    for (int i = 0; i < m; i++) {
        for (int j = i + 1; j < m; j++) {
            int g = arr[j] - arr[i];
            unsigned idx = hash2975(g) & (unsigned)(cap - 1);
            int existed = 0;
            unsigned ii = idx;
            while (hs[ii].used) {
                if (hs[ii].key == g) { existed = 1; break; }
                ii = (ii + 1) & (unsigned)(cap - 1);
            }
            if (!existed) {
                hsAdd2975(hs, cap, g);
                keys[kc++] = g;
            }
        }
    }
    free(arr);
    *outCap = cap;
    *outKeys = keys;
    *outKeyCount = kc;
    return hs;
}

int maximizeSquareArea(int m, int n, int* hFences, int hFencesSize, int* vFences, int vFencesSize) {
    const int mod = 1000000007;
    int hCap, vCap, hkc, vkc;
    int *hKeys, *vKeys;
    HS2975* hg = gaps2975(hFences, hFencesSize, m, &hCap, &hKeys, &hkc);
    HS2975* vg = gaps2975(vFences, vFencesSize, n, &vCap, &vKeys, &vkc);
    (void)vKeys;
    (void)vkc;
    int best = -1;
    for (int i = 0; i < hkc; i++) {
        int g = hKeys[i];
        if (hsHas2975(vg, vCap, g) && g - 1 > best) best = g - 1;
    }
    free(hg);
    free(vg);
    free(hKeys);
    free(vKeys);
    if (best < 0) return -1;
    return (int)(((long long)best * best) % mod);
}
