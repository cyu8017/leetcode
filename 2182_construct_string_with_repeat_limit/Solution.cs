// LeetCode 2182 - Construct String With Repeat Limit
// https://leetcode.com/problems/construct-string-with-repeat-limit/

public class Solution {
    public string RepeatLimitedString(string s, int repeatLimit) {
        int[] freq = new int[26];
        foreach (char c in s) freq[c - 'a']++;
        var ans = new System.Text.StringBuilder();
        while (true) {
            bool placed = false;
            for (int c = 25; c >= 0; c--) {
                if (freq[c] == 0) continue;
                if (ans.Length > 0 && ans[ans.Length - 1] - 'a' == c) {
                    bool found = false;
                    for (int d = c - 1; d >= 0; d--) {
                        if (freq[d] > 0) {
                            ans.Append((char)('a' + d));
                            freq[d]--;
                            found = placed = true;
                            break;
                        }
                    }
                    if (!found) return ans.ToString();
                    break;
                }
                int use = Math.Min(freq[c], repeatLimit);
                for (int i = 0; i < use; i++) ans.Append((char)('a' + c));
                freq[c] -= use;
                placed = true;
                break;
            }
            if (!placed) break;
        }
        return ans.ToString();
    }
}
