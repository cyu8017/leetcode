// LeetCode 3785 - Minimum Swaps to Avoid Forbidden Values
// https://leetcode.com/problems/minimum-swaps-to-avoid-forbidden-values/

#include <stdlib.h>

typedef struct { int key; int cnt; } Pair3785;

static int find3785(Pair3785* a, int n, int key) {
    for (int i = 0; i < n; i++) if (a[i].key == key) return i;
    return -1;
}

int minSwaps(int* nums, int numsSize, int* forbidden, int forbiddenSize) {
    (void)forbiddenSize;
    int n = numsSize;
    Pair3785* freq = (Pair3785*)malloc((size_t)(2 * n + 8) * sizeof(Pair3785));
    int fsz = 0;
    for (int i = 0; i < n; i++) {
        int idx = find3785(freq, fsz, nums[i]);
        if (idx < 0) { freq[fsz].key = nums[i]; freq[fsz].cnt = 1; fsz++; }
        else freq[idx].cnt++;
    }
    for (int i = 0; i < n; i++) {
        int idx = find3785(freq, fsz, forbidden[i]);
        if (idx < 0) { freq[fsz].key = forbidden[i]; freq[fsz].cnt = 1; fsz++; }
        else freq[idx].cnt++;
    }
    for (int i = 0; i < fsz; i++) {
        if (freq[i].cnt > n) { free(freq); return -1; }
    }
    Pair3785* bad = (Pair3785*)malloc((size_t)(n + 8) * sizeof(Pair3785));
    int bsz = 0, total = 0, largest = 0;
    for (int i = 0; i < n; i++) {
        if (nums[i] == forbidden[i]) {
            int idx = find3785(bad, bsz, nums[i]);
            if (idx < 0) { bad[bsz].key = nums[i]; bad[bsz].cnt = 1; idx = bsz++; }
            else bad[idx].cnt++;
            total++;
            if (bad[idx].cnt > largest) largest = bad[idx].cnt;
        }
    }
    free(freq); free(bad);
    if ((total + 1) / 2 > largest) return (total + 1) / 2;
    return largest;
}
