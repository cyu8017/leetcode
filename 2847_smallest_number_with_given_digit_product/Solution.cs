// LeetCode 2847 - Smallest Number With Given Digit Product
// https://leetcode.com/problems/smallest-number-with-given-digit-product/

using System;
using System.Text;

public class Solution {
    public string SmallestNumber(long n) {
        if (n == 0) return "0";
        if (n == 1) return "1";
        var digits = new StringBuilder();
        for (int d = 9; d >= 2; d--) {
            while (n % d == 0) {
                digits.Append((char)('0' + d));
                n /= d;
            }
        }
        if (n > 1) return "-1";
        var arr = digits.ToString().ToCharArray();
        Array.Reverse(arr);
        return new string(arr);
    }
}
