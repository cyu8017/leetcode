// LeetCode 3962 - Maximum Subarray Sum After at Most K Swaps
// https://leetcode.com/problems/maximum-subarray-sum-after-at-most-k-swaps/

#include <stdlib.h>
#include <string.h>

static int cmpInt3962(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

static int ULEN3962;

static void bitAdd3962(int* count, long long* sum, int* unique, int index, int delta) {
    long long value = unique[index - 1];
    for (; index < ULEN3962; index += index & -index) {
        count[index] += delta;
        sum[index] += (long long)delta * value;
    }
}
static int bitQueryCount3962(int* bit, int index) {
    int result = 0;
    for (; index > 0; index -= index & -index) result += bit[index];
    return result;
}
static long long bitQuerySum3962(long long* bit, int index) {
    long long result = 0;
    for (; index > 0; index -= index & -index) result += bit[index];
    return result;
}
static int bitKth3962(int* bit, int order) {
    int index = 0, step = 1;
    while ((step << 1) < ULEN3962) step <<= 1;
    for (; step > 0; step >>= 1) {
        int next = index + step;
        if (next < ULEN3962 && bit[next] < order) {
            index = next;
            order -= bit[next];
        }
    }
    return index + 1;
}
static long long sumSmallest3962(int* count, long long* sum, int* unique, int amount) {
    if (amount <= 0) return 0;
    int index = bitKth3962(count, amount);
    int countBefore = bitQueryCount3962(count, index - 1);
    long long sumBefore = bitQuerySum3962(sum, index - 1);
    return sumBefore + (long long)(amount - countBefore) * unique[index - 1];
}

long long maxSubarraySum(int* nums, int numsSize, int k) {
    int n = numsSize;
    int* values = malloc((size_t)n * sizeof(int));
    memcpy(values, nums, (size_t)n * sizeof(int));
    qsort(values, (size_t)n, sizeof(int), cmpInt3962);
    int m = 0;
    for (int i = 0; i < n; i++) if (m == 0 || values[m - 1] != values[i]) values[m++] = values[i];
    int* unique = values;
    ULEN3962 = m + 1;
    int* rank = malloc((size_t)n * sizeof(int));
    int* globalCount = calloc((size_t)(m + 1), sizeof(int));
    long long* globalSum = calloc((size_t)(m + 1), sizeof(long long));
    for (int i = 0; i < n; i++) {
        int lo = 0, hi = m;
        while (lo < hi) { int mid = (lo + hi) / 2; if (unique[mid] >= nums[i]) hi = mid; else lo = mid + 1; }
        rank[i] = lo + 1;
        bitAdd3962(globalCount, globalSum, unique, rank[i], 1);
    }
    long long answer = -(1LL << 60);
    for (int left = 0; left < n; left++) {
        int* insideCount = calloc((size_t)(m + 1), sizeof(int));
        long long* insideSum = calloc((size_t)(m + 1), sizeof(long long));
        int* outsideCount = malloc((size_t)(m + 1) * sizeof(int));
        long long* outsideSum = malloc((size_t)(m + 1) * sizeof(long long));
        memcpy(outsideCount, globalCount, (size_t)(m + 1) * sizeof(int));
        memcpy(outsideSum, globalSum, (size_t)(m + 1) * sizeof(long long));
        long long subarraySum = 0;
        for (int right = left; right < n; right++) {
            bitAdd3962(outsideCount, outsideSum, unique, rank[right], -1);
            bitAdd3962(insideCount, insideSum, unique, rank[right], 1);
            subarraySum += nums[right];
            int insideSize = right - left + 1;
            int outsideSize = n - insideSize;
            int limit = k;
            if (insideSize < limit) limit = insideSize;
            if (outsideSize < limit) limit = outsideSize;
            int low = 0, high = limit;
            while (low < high) {
                int mid = (low + high + 1) / 2;
                int insideValue = unique[bitKth3962(insideCount, mid) - 1];
                int outsideOrder = outsideSize - mid + 1;
                int outsideValue = unique[bitKth3962(outsideCount, outsideOrder) - 1];
                if (outsideValue > insideValue) low = mid;
                else high = mid - 1;
            }
            int swaps = low;
            long long gain = 0;
            if (swaps > 0) {
                long long smallInside = sumSmallest3962(insideCount, insideSum, unique, swaps);
                long long totalOutside = bitQuerySum3962(outsideSum, m);
                long long largeOutside = totalOutside - sumSmallest3962(outsideCount, outsideSum, unique, outsideSize - swaps);
                gain = largeOutside - smallInside;
            }
            if (subarraySum + gain > answer) answer = subarraySum + gain;
        }
        free(insideCount); free(insideSum); free(outsideCount); free(outsideSum);
    }
    free(values); free(rank); free(globalCount); free(globalSum);
    return answer;
}
