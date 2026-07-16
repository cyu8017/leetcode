// LeetCode 0263 - Ugly Number
// https://leetcode.com/problems/ugly-number/

class Solution {
    public boolean isUgly(int n) {
        if (n <= 0) {
            return false;
        }
        for (int factor : new int[] { 2, 3, 5 }) {
            while (n % factor == 0) {
                n /= factor;
            }
        }
        return n == 1;
    }
}
