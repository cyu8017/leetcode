// LeetCode 2281 - Sum of Total Strength of Wizards
// https://leetcode.com/problems/sum-of-total-strength-of-wizards/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int totalStrength(int[] strength) {
        final int mod = 1_000_000_007;
        int n = strength.length;
        int[] left = new int[n], right = new int[n];
        List<Integer> stack = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && strength[stack.get(stack.size() - 1)] >= strength[i])
                stack.remove(stack.size() - 1);
            left[i] = stack.isEmpty() ? -1 : stack.get(stack.size() - 1);
            stack.add(i);
        }
        stack.clear();
        for (int i = n - 1; i >= 0; i--) {
            while (!stack.isEmpty() && strength[stack.get(stack.size() - 1)] > strength[i])
                stack.remove(stack.size() - 1);
            right[i] = stack.isEmpty() ? n : stack.get(stack.size() - 1);
            stack.add(i);
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
        return (int) ans;
    }
}
