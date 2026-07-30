// LeetCode 1980 - Find Unique Binary String
// https://leetcode.com/problems/find-unique-binary-string/

using System;
using System.Collections.Generic;

public class Solution {
    public string FindDifferentBinaryString(string[] nums) {
        var s = new HashSet<string>(nums);
        int n = nums.Length;
        string[] preferred = { "11", "101", "00", "10", "01", "000", "001", "010", "011", "100", "110", "111" };
        foreach (var cand in preferred)
            if (cand.Length == n && !s.Contains(cand)) return cand;
        for (int i = 0; i < (1 << n); i++) {
            string cand = Convert.ToString(i, 2).PadLeft(n, '0');
            if (!s.Contains(cand)) return cand;
        }
        return new string('0', n);
    }
}