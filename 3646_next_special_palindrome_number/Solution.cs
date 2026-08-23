// LeetCode 3646 - Next Special Palindrome Number
// https://leetcode.com/problems/next-special-palindrome-number/

using System;
using System.Collections.Generic;
using System.Text;

public class Solution {
    public long SpecialPalindrome(long n) {
        var cands = new List<long>();
        void Gen(int mask) {
            int total = 0, odd = 0;
            for (int d = 1; d <= 9; d++) {
                if (((mask >> d) & 1) != 0) {
                    total += d;
                    if (d % 2 == 1) odd++;
                }
            }
            if (total == 0 || total > 18 || odd > 1) return;
            int[] halfCnt = new int[10];
            int mid = 0;
            for (int d = 1; d <= 9; d++) {
                if (((mask >> d) & 1) == 0) continue;
                halfCnt[d] = d / 2;
                if (d % 2 == 1) mid = d;
            }
            int halfLen = total / 2;
            void Dfs(int pos, List<int> cur) {
                if (pos == halfLen) {
                    var left = new StringBuilder();
                    foreach (int x in cur) left.Append((char)('0' + x));
                    var s = new StringBuilder(left.ToString());
                    if (mid > 0) s.Append((char)('0' + mid));
                    for (int i = left.Length - 1; i >= 0; i--) s.Append(left[i]);
                    cands.Add(long.Parse(s.ToString()));
                    return;
                }
                for (int d = 1; d <= 9; d++) {
                    if (halfCnt[d] == 0) continue;
                    halfCnt[d]--;
                    cur.Add(d);
                    Dfs(pos + 1, cur);
                    cur.RemoveAt(cur.Count - 1);
                    halfCnt[d]++;
                }
            }
            Dfs(0, new List<int>());
        }
        for (int mask = 1; mask < (1 << 10); mask++) {
            if ((mask & 1) != 0) continue;
            Gen(mask);
        }
        cands.Sort();
        foreach (long v in cands)
            if (v > n) return v;
        return -1;
    }
}
