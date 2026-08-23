// LeetCode 3714 - Longest Balanced Substring II
// https://leetcode.com/problems/longest-balanced-substring-ii/

using System;
using System.Collections.Generic;

public class Solution {
    int Calc1(string s) {
        int res = 0, n = s.Length, i = 0;
        while (i < n) {
            int j = i + 1;
            while (j < n && s[j] == s[i]) j++;
            res = Math.Max(res, j - i);
            i = j;
        }
        return res;
    }

    int Calc2(string s, char a, char b) {
        int res = 0, n = s.Length, i = 0;
        while (i < n) {
            while (i < n && s[i] != a && s[i] != b) i++;
            var pos = new Dictionary<int, int> { [0] = i - 1 };
            int d = 0;
            while (i < n && (s[i] == a || s[i] == b)) {
                if (s[i] == a) d++;
                else d--;
                if (pos.TryGetValue(d, out int p)) res = Math.Max(res, i - p);
                else pos[d] = i;
                i++;
            }
        }
        return res;
    }

    int Calc3(string s) {
        var pos = new Dictionary<(int, int), int> { [(0, 0)] = -1 };
        int[] cnt = new int[3];
        int res = 0;
        for (int i = 0; i < s.Length; i++) {
            cnt[s[i] - 'a']++;
            int x = cnt[0] - cnt[1], y = cnt[1] - cnt[2];
            var k = (x, y);
            if (pos.TryGetValue(k, out int p)) res = Math.Max(res, i - p);
            else pos[k] = i;
        }
        return res;
    }

    public int LongestBalanced(string s) {
        int x = Calc1(s);
        int y = Math.Max(Calc2(s, 'a', 'b'), Math.Max(Calc2(s, 'b', 'c'), Calc2(s, 'a', 'c')));
        int z = Calc3(s);
        return Math.Max(x, Math.Max(y, z));
    }
}
