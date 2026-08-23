// LeetCode 2847 - Smallest Number With Given Digit Product
// https://leetcode.com/problems/smallest-number-with-given-digit-product/

class Solution {
    public String smallestNumber(long n) {
        if (n == 0) return "0";
        if (n == 1) return "1";
        StringBuilder digits = new StringBuilder();
        for (int d = 9; d >= 2; d--) {
            while (n % d == 0) {
                digits.append((char) ('0' + d));
                n /= d;
            }
        }
        if (n > 1) return "-1";
        return digits.reverse().toString();
    }
}
