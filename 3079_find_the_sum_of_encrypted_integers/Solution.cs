// LeetCode 3079 - Find the Sum of Encrypted Integers
// https://leetcode.com/problems/find-the-sum-of-encrypted-integers/

using System;

public class Solution {
    static int Encrypt(int x) {
        int mx = 0, p = 0;
        for (; x > 0; x /= 10) {
            mx = Math.Max(mx, x % 10);
            p = p * 10 + 1;
        }
        return mx * p;
    }

    public int SumOfEncryptedInt(int[] nums) {
        int ans = 0;
        foreach (int x in nums) ans += Encrypt(x);
        return ans;
    }
}
