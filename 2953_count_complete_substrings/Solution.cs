// LeetCode 2953 - Count Complete Substrings
// https://leetcode.com/problems/count-complete-substrings/

using System;

public class Solution {
    public int CountCompleteSubstrings(string word, int k) {
        int n = word.Length, ans = 0;
        for (int i = 0; i < n; ) {
            int j = i;
            while (j + 1 < n && Math.Abs(word[j + 1] - word[j]) <= 2) j++;
            string seg = word.Substring(i, j - i + 1);
            int m = seg.Length;
            for (int chars = 1; chars <= 26; chars++) {
                int length = chars * k;
                if (length > m) break;
                int[] freq = new int[26];
                int unique = 0;
                for (int r = 0; r < m; r++) {
                    int c = seg[r] - 'a';
                    freq[c]++;
                    if (freq[c] == 1) unique++;
                    if (r >= length) {
                        int c2 = seg[r - length] - 'a';
                        freq[c2]--;
                        if (freq[c2] == 0) unique--;
                    }
                    if (r >= length - 1 && unique == chars) {
                        bool ok = true;
                        foreach (int f in freq)
                            if (f != 0 && f != k) { ok = false; break; }
                        if (ok) ans++;
                    }
                }
            }
            i = j + 1;
        }
        return ans;
    }
}
