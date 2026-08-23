// LeetCode 3662 - Filter Characters by Frequency
// https://leetcode.com/problems/filter-characters-by-frequency/

using System.Text;

public class Solution {
    public string FilterCharacters(string s, int k) {
        int[] cnt = new int[26];
        foreach (char c in s) cnt[c - 'a']++;
        var ans = new StringBuilder();
        foreach (char c in s)
            if (cnt[c - 'a'] < k) ans.Append(c);
        return ans.ToString();
    }
}
