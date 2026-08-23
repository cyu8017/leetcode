// LeetCode 2949 - Count Beautiful Substrings II
// https://leetcode.com/problems/count-beautiful-substrings-ii/

using System.Collections.Generic;

public class Solution {
    public long BeautifulSubstrings(string s, int k) {
        bool IsVowel(char c) => c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
        int x = 1;
        while ((x * x) % k != 0) x++;
        var freq = new Dictionary<(int, int), int>();
        freq[(0, 0)] = 1;
        int bal = 0, vowels = 0;
        long ans = 0;
        foreach (char ch in s) {
            if (IsVowel(ch)) { bal++; vowels++; }
            else bal--;
            var kk = (bal, vowels % x);
            freq.TryGetValue(kk, out int f);
            ans += f;
            freq[kk] = f + 1;
        }
        return ans;
    }
}
