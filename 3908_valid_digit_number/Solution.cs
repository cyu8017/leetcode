// LeetCode 3908 - Valid Digit Number
// https://leetcode.com/problems/valid-digit-number/

public class Solution {
    public bool ValidDigit(int n, int x) {
        bool hasX = false;
        while (n > 9) {
            hasX = hasX || (n % 10 == x);
            n /= 10;
        }
        return hasX && (n != x);
    }
}
