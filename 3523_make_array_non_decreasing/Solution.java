// LeetCode 3523 - Make Array Non-decreasing
// https://leetcode.com/problems/make-array-non-decreasing/

class Solution {
    public int maximumPossibleSize(int[] nums) {
        int ans = 0, mx = 0;
        for (int x : nums) {
            if (mx <= x) {
                ans++;
                mx = x;
            }
        }
        return ans;
    }
}
