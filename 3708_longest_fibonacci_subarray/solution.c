// LeetCode 3708 - Longest Fibonacci Subarray
// https://leetcode.com/problems/longest-fibonacci-subarray/

int longestSubarray(int* nums, int numsSize) {
    int f = 2, ans = 2;
    for (int i = 2; i < numsSize; i++) {
        if (nums[i] == nums[i - 1] + nums[i - 2]) {
            f++;
            if (f > ans) ans = f;
        } else f = 2;
    }
    return ans;
}
