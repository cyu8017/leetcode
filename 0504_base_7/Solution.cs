// LeetCode 0504 - Base 7
// https://leetcode.com/problems/base-7/

public class Solution {
    public string ConvertToBase7(int num) {
        if (num == 0) {
            return "0";
        }
        bool negative = num < 0;
        int value = Math.Abs(num);
        List<char> digits = new();
        while (value > 0) {
            digits.Add((char)('0' + value % 7));
            value /= 7;
        }
        digits.Reverse();
        string result = new string(digits.ToArray());
        return negative ? "-" + result : result;
    }
}
