// LeetCode 2255 - Count Prefixes of a Given String
// https://leetcode.com/problems/count-prefixes-of-a-given-string/

public class Solution {
    public int CountPrefixes(string[] words, string s) {
        int ans = 0;
        foreach (var w in words)
            if (w.Length <= s.Length && s.StartsWith(w)) ans++;
        return ans;
    }
}
