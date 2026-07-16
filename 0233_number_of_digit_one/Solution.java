// LeetCode 0233 - Number of Digit One
// https://leetcode.com/problems/number-of-digit-one/

class Solution {
    public int countDigitOne(int n) {
        long count = 0;
        long factor = 1;
        long value = n;
        while (factor <= value) {
            long lower = value % factor;
            long current = (value / factor) % 10;
            long higher = value / (factor * 10);
            if (current == 0) {
                count += higher * factor;
            } else if (current == 1) {
                count += higher * factor + lower + 1;
            } else {
                count += (higher + 1) * factor;
            }
            factor *= 10;
        }
        return (int) count;
    }
}
