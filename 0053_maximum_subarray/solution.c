// LeetCode 0053 - Maximum Subarray
// https://leetcode.com/problems/maximum-subarray/

int maxSubArray(int* nums, int numsSize) {
    int best = nums[0];
    int current = nums[0];

    for (int i = 1; i < numsSize; i++) {
        if (current + nums[i] > nums[i]) {
            current += nums[i];
        } else {
            current = nums[i];
        }
        if (current > best) {
            best = current;
        }
    }

    return best;
}
