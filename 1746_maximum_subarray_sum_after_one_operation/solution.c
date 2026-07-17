// LeetCode 1746 - Maximum Subarray Sum After One Operation
// https://leetcode.com/problems/maximum-subarray-sum-after-one-operation/

int maxSumAfterOperation(int* nums, int numsSize) {
    long long noSquare = 0;
    long long oneSquare = 0;
    long long best = -1000000000000000000LL;
    for (int i = 0; i < numsSize; i++) {
        long long v = nums[i];
        long long withSquare = oneSquare + v;
        if (noSquare + v * v > withSquare) withSquare = noSquare + v * v;
        if (v * v > withSquare) withSquare = v * v;
        oneSquare = withSquare;
        noSquare = noSquare + v > v ? noSquare + v : v;
        if (oneSquare > best) best = oneSquare;
    }
    return (int) best;
}
