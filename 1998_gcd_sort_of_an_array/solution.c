// LeetCode 1998 - GCD Sort of an Array
// https://leetcode.com/problems/gcd-sort-of-an-array/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

static int findP(int* parent, int x) {
    while (parent[x] != x) {
        parent[x] = parent[parent[x]];
        x = parent[x];
    }
    return x;
}

static void unite(int* parent, int a, int b) {
    a = findP(parent, a); b = findP(parent, b);
    if (a != b) parent[b] = a;
}

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

bool gcdSort(int* nums, int numsSize) {
    int m = nums[0];
    for (int i = 1; i < numsSize; i++) if (nums[i] > m) m = nums[i];
    int* parent = (int*)malloc((size_t)(m + 1) * sizeof(int));
    int* spf = (int*)malloc((size_t)(m + 1) * sizeof(int));
    for (int i = 0; i <= m; i++) { parent[i] = i; spf[i] = i; }
    for (int i = 2; i * i <= m; i++) {
        if (spf[i] == i) {
            for (int j = i * i; j <= m; j += i) {
                if (spf[j] == j) spf[j] = i;
            }
        }
    }
    char* seen = (char*)calloc((size_t)m + 1, 1);
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i];
        if (seen[x]) continue;
        seen[x] = 1;
        int y = x;
        while (y > 1) {
            int p = spf[y];
            unite(parent, x, p);
            while (y % p == 0) y /= p;
        }
    }
    int* sorted = (int*)malloc((size_t)numsSize * sizeof(int));
    memcpy(sorted, nums, (size_t)numsSize * sizeof(int));
    qsort(sorted, (size_t)numsSize, sizeof(int), cmpInt);
    bool ok = true;
    for (int i = 0; i < numsSize; i++) {
        if (findP(parent, nums[i]) != findP(parent, sorted[i])) { ok = false; break; }
    }
    free(parent); free(spf); free(seen); free(sorted);
    return ok;
}
