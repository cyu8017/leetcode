// LeetCode 2131 - Longest Palindrome by Concatenating Two Letter Words
// https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/

public class Solution {
    public int LongestPalindrome(string[] words) {
        var freq = new Dictionary<string, int>();
        foreach (string w in words) {
            if (!freq.ContainsKey(w)) freq[w] = 0;
            freq[w]++;
        }
        int ans = 0;
        bool center = false;
        foreach (var kv in freq) {
            string w = kv.Key;
            int c = kv.Value;
            string rev = new string(new[] { w[1], w[0] });
            if (w[0] == w[1]) {
                ans += (c / 2) * 4;
                if (c % 2 != 0) center = true;
            } else if (string.CompareOrdinal(w, rev) < 0) {
                ans += Math.Min(c, freq.GetValueOrDefault(rev)) * 4;
            }
        }
        if (center) ans += 2;
        return ans;
    }
}
