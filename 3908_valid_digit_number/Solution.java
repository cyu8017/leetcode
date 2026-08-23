// LeetCode 3908 - Valid Digit Number
// https://leetcode.com/problems/valid-digit-number/

class Solution {
    public boolean validDigit(int n, int x) {
        boolean hasX = false;
        while (n > 9) {
            hasX = hasX || (n % 10 == x);
            n /= 10;
        }
        return hasX && (n != x);
    }
}
