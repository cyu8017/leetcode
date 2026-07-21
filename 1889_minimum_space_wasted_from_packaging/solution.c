// LeetCode 1889 - Minimum Space Wasted From Packaging
// https://leetcode.com/problems/minimum-space-wasted-from-packaging/

#include <limits.h>
#include <stdlib.h>
#include <string.h>

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

int minWastedSpace(int* packages, int packagesSize, int** boxes, int boxesSize, int* boxesColSize) {
    qsort(packages, (size_t)packagesSize, sizeof(int), cmpAsc);
    long long* prefix = (long long*)malloc((size_t)packagesSize * sizeof(long long));
    prefix[0] = packages[0];
    for (int i = 1; i < packagesSize; i++) prefix[i] = prefix[i - 1] + packages[i];

    long long answer = LLONG_MAX;
    for (int s = 0; s < boxesSize; s++) {
        int* supplier = boxes[s];
        int m = boxesColSize[s];
        int* sorted = (int*)malloc((size_t)m * sizeof(int));
        memcpy(sorted, supplier, (size_t)m * sizeof(int));
        qsort(sorted, (size_t)m, sizeof(int), cmpAsc);
        int start = 0;
        long long wasted = 0;
        for (int b = 0; b < m; b++) {
            int end = upperBound(packages, start, packagesSize, sorted[b]);
            if (end == start) continue;
            long long packageSum = prefix[end - 1] - (start ? prefix[start - 1] : 0);
            wasted += (long long)sorted[b] * (end - start) - packageSum;
            start = end;
        }
        if (start == packagesSize && wasted < answer) answer = wasted;
        free(sorted);
    }
    free(prefix);
    return answer == LLONG_MAX ? -1 : (int)(answer % 1000000007LL);
}
