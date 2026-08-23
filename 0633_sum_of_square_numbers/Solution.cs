// LeetCode 0633 - Sum of Square Numbers
// https://leetcode.com/problems/sum-of-square-numbers/

public class Solution {
    public bool JudgeSquareSum(int c) {
        long left = 0;
        long right = (long)System.Math.Sqrt(c);
        while (left <= right) {
            long total = left * left + right * right;
            if (total == c) return true;
            if (total < c) ++left;
            else --right;
        }
        return false;
    }
}
