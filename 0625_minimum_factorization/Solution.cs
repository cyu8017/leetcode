// LeetCode 0625 - Minimum Factorization
// https://leetcode.com/problems/minimum-factorization/

using System.Collections.Generic;

public class Solution {
    public int SmallestFactorization(int num) {
        if (num < 10) return num;
        var digits = new List<int>();
        for (int digit = 9; digit >= 2; --digit) {
            while (num % digit == 0) {
                digits.Add(digit);
                num /= digit;
            }
        }
        if (num != 1) return 0;
        long result = 0;
        for (int i = digits.Count - 1; i >= 0; --i) {
            result = result * 10 + digits[i];
            if (result > int.MaxValue) return 0;
        }
        return (int)result;
    }
}
