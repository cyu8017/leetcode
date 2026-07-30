// LeetCode 1573 - Number of Ways to Split a String
// https://leetcode.com/problems/number-of-ways-to-split-a-string/

using System.Collections.Generic;

public class Solution {
    public int NumWays(string s) {
        const int MOD = 1000000007;
        int ones = 0;
        foreach (char ch in s) if (ch == '1') ones++;
        if (ones % 3 != 0) return 0;
        if (ones == 0) {
            long gaps = s.Length - 1;
            return (int)(gaps * (gaps - 1) / 2 % MOD);
        }
        int target = ones / 3;
        var positions = new List<int>();
        for (int i = 0; i < s.Length; i++)
            if (s[i] == '1') positions.Add(i);
        long ways = (long)(positions[target] - positions[target - 1]) *
                    (positions[2 * target] - positions[2 * target - 1]) % MOD;
        return (int)ways;
    }
}
