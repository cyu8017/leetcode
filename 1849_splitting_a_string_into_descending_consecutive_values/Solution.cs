// LeetCode 1849 - Splitting a String Into Descending Consecutive Values
// https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

using System.Numerics;

public class Solution {
    public bool SplitString(string s) {
        return Dfs(s, 0, null, 0);
    }

    private bool Dfs(string s, int index, BigInteger? previous, int parts) {
        if (index == s.Length) return parts >= 2;
        for (int end = index + 1; end <= s.Length; end++) {
            var value = BigInteger.Parse(s.Substring(index, end - index));
            if (previous == null) {
                if (Dfs(s, end, value, parts + 1)) return true;
            } else if (value == previous.Value - 1) {
                if (Dfs(s, end, value, parts + 1)) return true;
            } else if (value > previous.Value - 1) {
                break;
            }
        }
        return false;
    }
}
