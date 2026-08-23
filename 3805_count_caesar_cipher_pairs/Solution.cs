// LeetCode 3805 - Count Caesar Cipher Pairs
// https://leetcode.com/problems/count-caesar-cipher-pairs/

using System.Collections.Generic;

public class Solution {
    public long CountPairs(string[] words) {
        var cnt = new Dictionary<string, int>();
        foreach (string word in words) {
            char[] s = word.ToCharArray();
            int k = 'z' - s[0];
            for (int i = 1; i < s.Length; i++) {
                s[i] = (char)('a' + (s[i] - 'a' + k) % 26);
            }
            s[0] = 'z';
            string key = new string(s);
            if (!cnt.ContainsKey(key)) cnt[key] = 0;
            cnt[key]++;
        }
        long ans = 0;
        foreach (var v in cnt.Values) ans += (long)v * (v - 1) / 2;
        return ans;
    }
}
