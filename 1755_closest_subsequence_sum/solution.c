// LeetCode 1755 - Closest Subsequence Sum
// https://leetcode.com/problems/closest-subsequence-sum/

#include <stdlib.h>

static int compareLongLong(const void* a, const void* b) {
    long long x = *(const long long*) a;
    long long y = *(const long long*) b;
    if (x < y) return -1;
    if (x > y) return 1;
    return 0;
}

static long long* subsetSums(const int* arr, int size, long long* outCount) {
    long long count = 1LL << size;
    long long* vals = (long long*) malloc(count * sizeof(long long));
    vals[0] = 0;
    long long filled = 1;
    for (int idx = 0; idx < size; idx++) {
        for (long long i = 0; i < filled; i++) {
            vals[filled + i] = vals[i] + arr[idx];
        }
        filled *= 2;
    }
    qsort(vals, count, sizeof(long long), compareLongLong);
    *outCount = count;
    return vals;
}

static long long llabsVal(long long v) {
    return v < 0 ? -v : v;
}

int minAbsDifference(int* nums, int numsSize, int goal) {
    int half = numsSize / 2;
    long long aCount;
    long long bCount;
    long long* a = subsetSums(nums, half, &aCount);
    long long* b = subsetSums(nums + half, numsSize - half, &bCount);

    long long best = -1;
    long long j = bCount - 1;
    for (long long i = 0; i < aCount; i++) {
        long long x = a[i];
        while (j > 0 && llabsVal(x + b[j] - goal) >= llabsVal(x + b[j - 1] - goal)) {
            j--;
        }
        long long diff = llabsVal(x + b[j] - goal);
        if (best < 0 || diff < best) {
            best = diff;
        }
    }

    free(a);
    free(b);
    return (int) best;
}
