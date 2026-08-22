// LeetCode 2202 - Maximize the Topmost Element After K Moves
// https://leetcode.com/problems/maximize-the-topmost-element-after-k-moves/

int maximumTop(int* nums, int numsSize, int k) {
    int n = numsSize;
    if (n == 1) return (k % 2 == 1) ? -1 : nums[0];
    if (k == 0) return nums[0];
    int ans = -1;
    int limit = k - 1;
    if (limit > n) limit = n;
    for (int i = 0; i < limit; i++) if (nums[i] > ans) ans = nums[i];
    if (k < n && nums[k] > ans) ans = nums[k];
    return ans;
}
