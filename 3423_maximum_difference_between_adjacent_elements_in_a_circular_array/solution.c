// LeetCode 3423 - Maximum Difference Between Adjacent Elements in a Circular Array
// https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/

int maxAdjacentDistance(int* nums, int numsSize) {
    int ans = 0, n = numsSize;
    for (int i = 0; i < n; i++) {
        int d = nums[i] - nums[(i + 1) % n];
        if (d < 0) d = -d;
        if (d > ans) ans = d;
    }
    return ans;
}
