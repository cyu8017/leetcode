// LeetCode 2148 - Count Elements With Strictly Smaller and Greater Elements
// https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/

class Solution {
    public int countElements(int[] nums) {
        int mn = nums[0], mx = nums[0];
        for (int x : nums) { mn = Math.min(mn, x); mx = Math.max(mx, x); }
        int ans = 0;
        for (int x : nums) if (x > mn && x < mx) ans++;
        return ans;
    }
}
