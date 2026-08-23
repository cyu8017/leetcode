// LeetCode 3862 - Find The Smallest Balanced Index
// https://leetcode.com/problems/find-the-smallest-balanced-index/

class Solution {
    public int smallestBalancedIndex(int[] nums) {
        long s = 0, p = 1;
        for (int x : nums) s += x;
        for (int i = nums.length - 1; i >= 0; i--) {
            s -= nums[i];
            if (s == p) return i;
            p *= nums[i];
            if (p >= s) break;
        }
        return -1;
    }
}
