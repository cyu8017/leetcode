// LeetCode 2251 - Number of Flowers in Full Bloom
// https://leetcode.com/problems/number-of-flowers-in-full-bloom/

#include <stdlib.h>

static int cmp_int(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

static int upper_bound(int* a, int n, int x) {
    int lo = 0, hi = n;
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (a[mid] <= x) lo = mid + 1;
        else hi = mid;
    }
    return lo;
}

static int lower_bound(int* a, int n, int x) {
    int lo = 0, hi = n;
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (a[mid] < x) lo = mid + 1;
        else hi = mid;
    }
    return lo;
}

int* fullBloomFlowers(int** flowers, int flowersSize, int* flowersColSize, int* people, int peopleSize, int* returnSize) {
    (void)flowersColSize;
    int* start = (int*)malloc((size_t)flowersSize * sizeof(int));
    int* end = (int*)malloc((size_t)flowersSize * sizeof(int));
    for (int i = 0; i < flowersSize; i++) {
        start[i] = flowers[i][0];
        end[i] = flowers[i][1];
    }
    qsort(start, (size_t)flowersSize, sizeof(int), cmp_int);
    qsort(end, (size_t)flowersSize, sizeof(int), cmp_int);
    int* ans = (int*)malloc((size_t)peopleSize * sizeof(int));
    for (int i = 0; i < peopleSize; i++) {
        int t = people[i];
        int started = upper_bound(start, flowersSize, t); // count start[j] <= t => first > t
        int ended = lower_bound(end, flowersSize, t);     // count end[j] < t
        ans[i] = started - ended;
    }
    free(start);
    free(end);
    *returnSize = peopleSize;
    return ans;
}
