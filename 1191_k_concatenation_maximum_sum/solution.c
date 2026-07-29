// LeetCode 1191 - K-Concatenation Maximum Sum
// https://leetcode.com/problems/k-concatenation-maximum-sum/

#include <stdlib.h>

static int kadane(int* nums, int numsSize) {
    int best = 0;
    int cur = 0;
    for (int i = 0; i < numsSize; i++) {
        cur = cur + nums[i] > 0 ? cur + nums[i] : 0;
        if (cur > best) best = cur;
    }
    return best;
}

int kConcatenationMaxSum(int* arr, int arrSize, int k) {
    const int MOD = 1000000007;
    int one = kadane(arr, arrSize);
    if (k == 1) return one % MOD;
    int* doubled = (int*)malloc((size_t)arrSize * 2 * sizeof(int));
    for (int i = 0; i < arrSize; i++) {
        doubled[i] = arr[i];
        doubled[i + arrSize] = arr[i];
    }
    int two = kadane(doubled, arrSize * 2);
    free(doubled);
    long long total = 0;
    for (int i = 0; i < arrSize; i++) total += arr[i];
    long long ans;
    if (total > 0) {
        ans = one;
        long long candidate = (long long)two + total * (k - 2);
        if (candidate > ans) ans = candidate;
    } else {
        ans = one > two ? one : two;
    }
    return (int)(ans % MOD);
}
