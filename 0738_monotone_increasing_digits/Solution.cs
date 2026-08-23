// LeetCode 0738 - Monotone Increasing Digits
// https://leetcode.com/problems/monotone-increasing-digits/

public class Solution {
    public int MonotoneIncreasingDigits(int n) {
        char[] digits = n.ToString().ToCharArray();
        int mark = digits.Length;
        for (int i = digits.Length - 1; i > 0; i--) {
            if (digits[i] < digits[i - 1]) {
                digits[i - 1] = (char)(digits[i - 1] - 1);
                mark = i;
            }
        }
        for (int i = mark; i < digits.Length; i++) digits[i] = '9';
        return int.Parse(new string(digits));
    }
}
