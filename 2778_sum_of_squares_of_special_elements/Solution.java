// LeetCode 2778 - Sum of Squares of Special Elements
// https://leetcode.com/problems/sum-of-squares-of-special-elements/

class Solution {
    public int sumOfSquares(int[] nums) {
        int n = nums.length, ans = 0;
        for (int i = 0; i < n; i++) {
            if (n % (i + 1) == 0) ans += nums[i] * nums[i];
        }
        return ans;
    }
}
