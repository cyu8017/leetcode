// LeetCode 0633 - Sum of Square Numbers
// https://leetcode.com/problems/sum-of-square-numbers/

class Solution {
    public boolean judgeSquareSum(int c) {
        long left = 0;
        long right = (long) Math.sqrt(c);
        while (left <= right) {
            long total = left * left + right * right;
            if (total == c) {
                return true;
            }
            if (total < c) {
                ++left;
            } else {
                --right;
            }
        }
        return false;
    }
}
