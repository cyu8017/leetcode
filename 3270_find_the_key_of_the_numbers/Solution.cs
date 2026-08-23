// LeetCode 3270 - Find the Key of the Numbers
// https://leetcode.com/problems/find-the-key-of-the-numbers/

using System;

public class Solution {
    public int GenerateKey(int num1, int num2, int num3) {
        int ans = 0, mul = 1;
        for (int t = 0; t < 4; t++) {
            int d = Math.Min(num1 % 10, Math.Min(num2 % 10, num3 % 10));
            ans += d * mul;
            mul *= 10;
            num1 /= 10; num2 /= 10; num3 /= 10;
        }
        return ans;
    }
}
