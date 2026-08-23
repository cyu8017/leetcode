// LeetCode 2544 - Alternating Digit Sum
// https://leetcode.com/problems/alternating-digit-sum/

class Solution {
    public int alternateDigitSum(int n) {
        int[] digits = new int[12];
        int len = 0, x = n;
        while (x > 0) {
            digits[len++] = x % 10;
            x /= 10;
        }
        int ans = 0, sign = 1;
        for (int i = len - 1; i >= 0; --i) {
            ans += sign * digits[i];
            sign = -sign;
        }
        return ans;
    }
}
