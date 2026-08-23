// LeetCode 2067 - Number of Equal Count Substrings
// https://leetcode.com/problems/number-of-equal-count-substrings/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int EqualCountSubstrings(string s, int count) {
        int ans = 0, n = s.Length;
        int maxUnique = s.Distinct().Count();
        for (int u = 1; u <= maxUnique; u++) {
            int needLen = u * count;
            if (needLen > n) break;
            int[] freq = new int[26];
            int have = 0;
            for (int i = 0; i < n; i++) {
                int c = s[i] - 'a';
                freq[c]++;
                if (freq[c] == count) have++;
                else if (freq[c] == count + 1) have--;
                if (i >= needLen) {
                    int p = s[i - needLen] - 'a';
                    if (freq[p] == count) have--;
                    else if (freq[p] == count + 1) have++;
                    freq[p]--;
                }
                if (i + 1 >= needLen && have == u) ans++;
            }
        }
        return ans;
    }
}
