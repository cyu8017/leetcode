// LeetCode 3523 - Make Array Non-decreasing
// https://leetcode.com/problems/make-array-non-decreasing/

public class Solution {
    public int MaximumPossibleSize(int[] nums) {
        int ans = 0, mx = 0;
        foreach (int x in nums) {
            if (mx <= x) {
                ans++;
                mx = x;
            }
        }
        return ans;
    }
}
