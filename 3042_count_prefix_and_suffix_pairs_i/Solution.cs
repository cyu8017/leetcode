// LeetCode 3042 - Count Prefix and Suffix Pairs I
// https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/

public class Solution {
    public int CountPrefixSuffixPairs(string[] words) {
        int ans = 0;
        for (int i = 0; i < words.Length; i++) {
            string s = words[i];
            for (int j = i + 1; j < words.Length; j++) {
                string t = words[j];
                if (t.Length >= s.Length && t.StartsWith(s) && t.EndsWith(s))
                    ans++;
            }
        }
        return ans;
    }
}
