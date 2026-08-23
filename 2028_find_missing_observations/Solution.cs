// LeetCode 2028 - Find Missing Observations
// https://leetcode.com/problems/find-missing-observations/

using System;

public class Solution {
    public int[] MissingRolls(int[] rolls, int mean, int n) {
        int sum = 0;
        foreach (int r in rolls) sum += r;
        int remain = mean * (rolls.Length + n) - sum;
        if (remain < n || remain > 6 * n) return Array.Empty<int>();
        int[] ans = new int[n];
        int baseVal = remain / n, extra = remain % n;
        for (int i = 0; i < n; i++) ans[i] = baseVal + (i < extra ? 1 : 0);
        return ans;
    }
}
