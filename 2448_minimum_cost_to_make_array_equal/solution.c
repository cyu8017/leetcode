// LeetCode 2448 - Minimum Cost to Make Array Equal
// https://leetcode.com/problems/minimum-cost-to-make-array-equal/

#include <stdlib.h>

typedef struct { int num; int cost; } Pair2448;

static int cmp2448(const void* a, const void* b) {
    return ((const Pair2448*)a)->num - ((const Pair2448*)b)->num;
}

long long minCost(int* nums, int numsSize, int* cost, int costSize) {
    (void)costSize;
    Pair2448* arr = (Pair2448*)malloc((size_t)numsSize * sizeof(Pair2448));
    long long totalCost = 0;
    for (int i = 0; i < numsSize; i++) {
        arr[i].num = nums[i];
        arr[i].cost = cost[i];
        totalCost += cost[i];
    }
    qsort(arr, (size_t)numsSize, sizeof(Pair2448), cmp2448);
    long long pref = 0;
    int median = 0;
    for (int i = 0; i < numsSize; i++) {
        pref += arr[i].cost;
        if (pref * 2 >= totalCost) {
            median = arr[i].num;
            break;
        }
    }
    long long ans = 0;
    for (int i = 0; i < numsSize; i++) {
        long long diff = nums[i] - median;
        if (diff < 0) diff = -diff;
        ans += diff * cost[i];
    }
    free(arr);
    return ans;
}
