// LeetCode 2185 - Counting Words With a Given Prefix
// https://leetcode.com/problems/counting-words-with-a-given-prefix/

public class Solution {
    public int PrefixCount(string[] words, string pref) {
        int ans = 0;
        foreach (string w in words)
            if (w.Length >= pref.Length && w.StartsWith(pref)) ans++;
        return ans;
    }
}
