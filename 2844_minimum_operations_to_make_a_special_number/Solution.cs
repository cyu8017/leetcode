// LeetCode 2844 - Minimum Operations to Make a Special Number
// https://leetcode.com/problems/minimum-operations-to-make-a-special-number/

using System;

public class Solution {
    public int MinimumOperations(string num) {
        int n = num.Length;
        int ans = n;
        bool has0 = false;
        foreach (char c in num) if (c == '0') has0 = true;
        if (has0) ans = Math.Min(ans, n - 1);
        string[] targets = { "00", "25", "50", "75" };
        foreach (string t in targets) {
            int j = n - 1;
            while (j >= 0 && num[j] != t[1]) j--;
            if (j < 0) continue;
            int i = j - 1;
            while (i >= 0 && num[i] != t[0]) i--;
            if (i < 0) continue;
            ans = Math.Min(ans, n - i - 2);
        }
        return ans;
    }
}
