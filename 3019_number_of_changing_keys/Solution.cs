// LeetCode 3019 - Number of Changing Keys
// https://leetcode.com/problems/number-of-changing-keys/

using System;

public class Solution {
    public int CountKeyChanges(string s) {
        s = s.ToLowerInvariant();
        int ans = 0;
        for (int i = 1; i < s.Length; i++)
            if (s[i] != s[i - 1]) ans++;
        return ans;
    }
}
