// LeetCode 0556 - Next Greater Element III
// https://leetcode.com/problems/next-greater-element-iii/

class Solution {
    public int nextGreaterElement(int n) {
        char[] digits = String.valueOf(n).toCharArray();
        int i = digits.length - 2;
        while (i >= 0 && digits[i] >= digits[i + 1]) {
            --i;
        }
        if (i < 0) {
            return -1;
        }

        int j = digits.length - 1;
        while (digits[j] <= digits[i]) {
            --j;
        }
        char tmp = digits[i];
        digits[i] = digits[j];
        digits[j] = tmp;

        reverse(digits, i + 1, digits.length - 1);

        long value = 0;
        for (char ch : digits) {
            value = value * 10 + (ch - '0');
        }
        if (value > Integer.MAX_VALUE) {
            return -1;
        }
        return (int) value;
    }

    private void reverse(char[] digits, int left, int right) {
        while (left < right) {
            char tmp = digits[left];
            digits[left] = digits[right];
            digits[right] = tmp;
            ++left;
            --right;
        }
    }
}
