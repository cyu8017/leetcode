// LeetCode 0556 - Next Greater Element III
// https://leetcode.com/problems/next-greater-element-iii/

public class Solution {
    public int NextGreaterElement(int n) {
        char[] digits = n.ToString().ToCharArray();
        int i = digits.Length - 2;
        while (i >= 0 && digits[i] >= digits[i + 1]) --i;
        if (i < 0) return -1;

        int j = digits.Length - 1;
        while (digits[j] <= digits[i]) --j;
        (digits[i], digits[j]) = (digits[j], digits[i]);
        System.Array.Reverse(digits, i + 1, digits.Length - i - 1);

        long value = 0;
        foreach (char ch in digits) value = value * 10 + (ch - '0');
        if (value > int.MaxValue) return -1;
        return (int)value;
    }
}
