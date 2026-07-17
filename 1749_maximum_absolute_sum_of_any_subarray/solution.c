// LeetCode 1749 - Maximum Absolute Sum of Any Subarray
// https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

int maxAbsoluteSum(int* nums, int numsSize) {
    int prefix = 0;
    int low = 0;
    int high = 0;
    for (int i = 0; i < numsSize; i++) {
        prefix += nums[i];
        if (prefix < low) low = prefix;
        if (prefix > high) high = prefix;
    }
    return high - low;
}
