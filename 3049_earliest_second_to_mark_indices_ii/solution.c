// LeetCode 3049 - Earliest Second to Mark Indices II
// https://leetcode.com/problems/earliest-second-to-mark-indices-ii/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

typedef struct { int* a; int n, cap; } MinHeap;
static void hpush(MinHeap* h, int x) {
    if (h->n == h->cap) { h->cap = h->cap ? h->cap * 2 : 16; h->a = (int*)realloc(h->a, (size_t)h->cap * sizeof(int)); }
    int i = h->n++; h->a[i] = x;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h->a[p] <= h->a[i]) break;
        int t = h->a[p]; h->a[p] = h->a[i]; h->a[i] = t; i = p;
    }
}
static int hpop(MinHeap* h) {
    int r = h->a[0];
    h->a[0] = h->a[--h->n];
    int i = 0;
    for (;;) {
        int l = 2 * i + 1, rg = 2 * i + 2, m = i;
        if (l < h->n && h->a[l] < h->a[m]) m = l;
        if (rg < h->n && h->a[rg] < h->a[m]) m = rg;
        if (m == i) break;
        int t = h->a[i]; h->a[i] = h->a[m]; h->a[m] = t; i = m;
    }
    return r;
}

/* secondToIndex[second] = index, -1 if none; size = m */
static int* getSecondToIndex(int* nums, int n, int* changeIndices, int m) {
    int* indexToFirst = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) indexToFirst[i] = -1;
    for (int second = 0; second < m; second++) {
        int index = changeIndices[second] - 1;
        if (nums[index] > 0 && indexToFirst[index] == -1) indexToFirst[index] = second;
    }
    int* secondToIndex = (int*)malloc((size_t)m * sizeof(int));
    for (int i = 0; i < m; i++) secondToIndex[i] = -1;
    for (int index = 0; index < n; index++) {
        if (indexToFirst[index] != -1) secondToIndex[indexToFirst[index]] = index;
    }
    free(indexToFirst);
    return secondToIndex;
}

static bool canMark(int* nums, int n, int* secondToIndex, int maxSecond, long long numsSum) {
    MinHeap h = {NULL, 0, 0};
    int marks = 0;
    for (int second = maxSecond - 1; second >= 0; second--) {
        int index = secondToIndex[second];
        if (index != -1) {
            hpush(&h, nums[index]);
            if (marks == 0) { hpop(&h); marks++; }
            else marks--;
        } else marks++;
    }
    int heapSize = h.n;
    long long heapSum = 0;
    while (h.n > 0) heapSum += hpop(&h);
    long long decrementAndMarkCost = numsSum - heapSum + (n - heapSize);
    long long zeroAndMarkCost = (long long)heapSize + heapSize;
    free(h.a);
    return decrementAndMarkCost + zeroAndMarkCost <= maxSecond;
}

int earliestSecondToMarkIndices(int* nums, int numsSize, int* changeIndices, int changeIndicesSize) {
    int* secondToIndex = getSecondToIndex(nums, numsSize, changeIndices, changeIndicesSize);
    long long numsSum = 0;
    for (int i = 0; i < numsSize; i++) numsSum += nums[i];
    int l = 0, r = changeIndicesSize + 1;
    while (l < r) {
        int mid = (l + r) / 2;
        if (canMark(nums, numsSize, secondToIndex, mid, numsSum)) r = mid;
        else l = mid + 1;
    }
    free(secondToIndex);
    return l <= changeIndicesSize ? l : -1;
}
