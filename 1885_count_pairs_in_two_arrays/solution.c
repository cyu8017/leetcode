// LeetCode 1885 - Count Pairs in Two Arrays
// https://leetcode.com/problems/count-pairs-in-two-arrays/

#include <stdlib.h>

static int cmpAsc(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

static int upperBound(int* arr, int lo, int hi, int target) {
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (arr[mid] <= target) lo = mid + 1;
        else hi = mid;
    }
    return lo;
}

long long countPairs(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    (void)nums2Size;
    int n = nums1Size;
    int* diff = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) diff[i] = nums1[i] - nums2[i];
    qsort(diff, (size_t)n, sizeof(int), cmpAsc);
    long long answer = 0;
    for (int i = 0; i < n; i++) {
        int pos = upperBound(diff, i + 1, n, -diff[i]);
        answer += n - pos;
    }
    free(diff);
    return answer;
}
