// LeetCode 2281 - Sum of Total Strength of Wizards
// https://leetcode.com/problems/sum-of-total-strength-of-wizards/

using System.Collections.Generic;

public class Solution {
    public int TotalStrength(int[] strength) {
        const int mod = 1000000007;
        int n = strength.Length;
        int[] left = new int[n], right = new int[n];
        var stack = new List<int>();
        for (int i = 0; i < n; i++) {
            while (stack.Count > 0 && strength[stack[stack.Count - 1]] >= strength[i]) stack.RemoveAt(stack.Count - 1);
            left[i] = stack.Count == 0 ? -1 : stack[stack.Count - 1];
            stack.Add(i);
        }
        stack.Clear();
        for (int i = n - 1; i >= 0; i--) {
            while (stack.Count > 0 && strength[stack[stack.Count - 1]] > strength[i]) stack.RemoveAt(stack.Count - 1);
            right[i] = stack.Count == 0 ? n : stack[stack.Count - 1];
            stack.Add(i);
        }
        long[] pref = new long[n + 1], prefPref = new long[n + 2];
        for (int i = 0; i < n; i++) pref[i + 1] = (pref[i] + strength[i]) % mod;
        for (int i = 0; i <= n; i++) prefPref[i + 1] = (prefPref[i] + pref[i]) % mod;
        long ans = 0;
        for (int i = 0; i < n; i++) {
            int l = left[i] + 1, r = right[i] - 1;
            long leftSum = (prefPref[i + 1] - prefPref[l] + mod) % mod;
            long rightSum = (prefPref[r + 2] - prefPref[i + 1] + mod) % mod;
            long leftCnt = i - l + 1, rightCnt = r - i + 1;
            long contrib = (rightCnt * leftSum % mod - leftCnt * rightSum % mod + mod) % mod;
            ans = (ans + contrib * strength[i] % mod) % mod;
        }
        return (int)ans;
    }
}
