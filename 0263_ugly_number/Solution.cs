// LeetCode 0263 - Ugly Number
// https://leetcode.com/problems/ugly-number/

public class Solution {
    public bool IsUgly(int n) {
        if (n <= 0) {
            return false;
        }
        foreach (int factor in new[] { 2, 3, 5 }) {
            while (n % factor == 0) {
                n /= factor;
            }
        }
        return n == 1;
    }
}
