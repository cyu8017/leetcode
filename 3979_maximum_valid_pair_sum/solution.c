// LeetCode 3979 - Maximum Valid Pair Sum
// https://leetcode.com/problems/maximum-valid-pair-sum/

int maxValidPairSum(int* nums, int numsSize, int k) {
    int ans = 0, x = 0;
    for (int j = k; j < numsSize; j++) {
        int y = nums[j];
        if (nums[j - k] > x) x = nums[j - k];
        if (x + y > ans) ans = x + y;
    }
    return ans;
}
