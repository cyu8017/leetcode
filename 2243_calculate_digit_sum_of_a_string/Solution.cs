// LeetCode 2243 - Calculate Digit Sum of a String
// https://leetcode.com/problems/calculate-digit-sum-of-a-string/

using System;
using System.Text;

public class Solution {
    public string DigitSum(string s, int k) {
        while (s.Length > k) {
            var next = new StringBuilder();
            for (int i = 0; i < s.Length; i += k) {
                int sum = 0;
                int end = Math.Min(i + k, s.Length);
                for (int j = i; j < end; j++) sum += s[j] - '0';
                next.Append(sum);
            }
            s = next.ToString();
        }
        return s;
    }
}
