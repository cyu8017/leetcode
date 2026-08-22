// LeetCode 3909 - Compare Sums Of Bitonic Parts
// https://leetcode.com/problems/compare-sums-of-bitonic-parts/

int compareBitonicSums(int* nums, int numsSize) {
    long long l = nums[0], r = 0;
    for (int i = 0; i < numsSize; i++) r += nums[i];
    for (int i = 1; i < numsSize; i++) {
        if (nums[i - 1] > nums[i]) break;
        l += nums[i];
        r -= nums[i - 1];
    }
    if (l == r) return -1;
    if (l > r) return 0;
    return 1;
}
