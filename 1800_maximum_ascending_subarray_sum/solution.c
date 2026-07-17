// LeetCode 1800 - Maximum Ascending Subarray Sum
// https://leetcode.com/problems/maximum-ascending-subarray-sum/

int maxAscendingSum(int* nums, int numsSize) {
    int best = nums[0];
    int cur = nums[0];
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] > nums[i - 1]) {
            cur += nums[i];
        } else {
            cur = nums[i];
        }
        if (cur > best) best = cur;
    }
    return best;
}
