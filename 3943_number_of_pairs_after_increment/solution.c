// LeetCode 3943 - Number of Pairs After Increment
// https://leetcode.com/problems/number-of-pairs-after-increment/

#include <stdlib.h>
#include <string.h>

enum { BS3943 = 225, HS3943 = 10007 };

typedef struct { int key, val, used; } Ent3943;

static void htClear3943(Ent3943* ht) { memset(ht, 0, HS3943 * sizeof(Ent3943)); }
static void htAdd3943(Ent3943* ht, int key, int delta) {
    unsigned h = (unsigned)key % HS3943;
    for (;;) {
        if (!ht[h].used) { ht[h].used = 1; ht[h].key = key; ht[h].val = delta; return; }
        if (ht[h].key == key) { ht[h].val += delta; return; }
        h = (h + 1) % HS3943;
    }
}
static int htGet3943(Ent3943* ht, int key) {
    unsigned h = (unsigned)key % HS3943;
    for (;;) {
        if (!ht[h].used) return 0;
        if (ht[h].key == key) return ht[h].val;
        h = (h + 1) % HS3943;
    }
}

long long* numberOfPairs(int* nums1, int nums1Size, int* nums2, int nums2Size, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)queriesColSize;
    int n = nums2Size;
    int blocks = (n + BS3943 - 1) / BS3943;
    int* lazy = calloc((size_t)blocks, sizeof(int));
    Ent3943** freq = malloc((size_t)blocks * sizeof(Ent3943*));
    for (int b = 0; b < blocks; b++) {
        freq[b] = calloc(HS3943, sizeof(Ent3943));
        int end = (b + 1) * BS3943; if (end > n) end = n;
        for (int i = b * BS3943; i < end; i++) htAdd3943(freq[b], nums2[i], 1);
    }
    Ent3943* fixed = calloc(HS3943, sizeof(Ent3943));
    int* fixedKeys = malloc((size_t)nums1Size * sizeof(int));
    int fkn = 0;
    for (int i = 0; i < nums1Size; i++) {
        if (htGet3943(fixed, nums1[i]) == 0) fixedKeys[fkn++] = nums1[i];
        htAdd3943(fixed, nums1[i], 1);
    }
    long long* answer = malloc((size_t)queriesSize * sizeof(long long));
    int an = 0;
    for (int qi = 0; qi < queriesSize; qi++) {
        int* q = queries[qi];
        if (q[0] == 1) {
            int l = q[1], r = q[2], delta = q[3];
            int first = l / BS3943, last = r / BS3943;
            if (first == last) {
                if (lazy[first]) {
                    int end = (first + 1) * BS3943; if (end > n) end = n;
                    for (int i = first * BS3943; i < end; i++) nums2[i] += lazy[first];
                    lazy[first] = 0;
                }
                for (int i = l; i <= r; i++) nums2[i] += delta;
                htClear3943(freq[first]);
                int end = (first + 1) * BS3943; if (end > n) end = n;
                for (int i = first * BS3943; i < end; i++) htAdd3943(freq[first], nums2[i], 1);
                continue;
            }
            if (lazy[first]) {
                int end = (first + 1) * BS3943;
                for (int i = first * BS3943; i < end; i++) nums2[i] += lazy[first];
                lazy[first] = 0;
            }
            for (int i = l; i < (first + 1) * BS3943; i++) nums2[i] += delta;
            htClear3943(freq[first]);
            for (int i = first * BS3943; i < (first + 1) * BS3943; i++) htAdd3943(freq[first], nums2[i], 1);
            if (lazy[last]) {
                int end = (last + 1) * BS3943; if (end > n) end = n;
                for (int i = last * BS3943; i < end; i++) nums2[i] += lazy[last];
                lazy[last] = 0;
            }
            for (int i = last * BS3943; i <= r; i++) nums2[i] += delta;
            htClear3943(freq[last]);
            int end = (last + 1) * BS3943; if (end > n) end = n;
            for (int i = last * BS3943; i < end; i++) htAdd3943(freq[last], nums2[i], 1);
            for (int b = first + 1; b < last; b++) lazy[b] += delta;
        } else {
            long long total = 0;
            for (int fi = 0; fi < fkn; fi++) {
                int a = fixedKeys[fi];
                int countA = htGet3943(fixed, a);
                int target = q[1] - a;
                for (int b = 0; b < blocks; b++)
                    total += (long long)countA * htGet3943(freq[b], target - lazy[b]);
            }
            answer[an++] = total;
        }
    }
    for (int b = 0; b < blocks; b++) free(freq[b]);
    free(freq); free(lazy); free(fixed); free(fixedKeys);
    *returnSize = an;
    return answer;
}
