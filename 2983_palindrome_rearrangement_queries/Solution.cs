// LeetCode 2983 - Palindrome Rearrangement Queries
// https://leetcode.com/problems/palindrome-rearrangement-queries/

using System;
using System.Collections.Generic;

public class Solution {
    public IList<bool> CanMakePalindromeQueries(string s, int[][] queries) {
        int n = s.Length;
        int m = n / 2;
        char[] tArr = s.Substring(m).ToCharArray();
        Array.Reverse(tArr);
        string t = new string(tArr);
        s = s.Substring(0, m);

        int[][] pre1 = new int[m + 1][];
        int[][] pre2 = new int[m + 1][];
        int[] diff = new int[m + 1];
        pre1[0] = new int[26];
        pre2[0] = new int[26];
        for (int i = 1; i <= m; ++i) {
            pre1[i] = (int[])pre1[i - 1].Clone();
            pre2[i] = (int[])pre2[i - 1].Clone();
            ++pre1[i][s[i - 1] - 'a'];
            ++pre2[i][t[i - 1] - 'a'];
            diff[i] = diff[i - 1] + (s[i - 1] == t[i - 1] ? 0 : 1);
        }

        var ans = new bool[queries.Length];
        for (int i = 0; i < queries.Length; ++i) {
            var q = queries[i];
            int a = q[0], b = q[1];
            int c = n - 1 - q[3], d = n - 1 - q[2];
            ans[i] = (a <= c) ? Check(pre1, pre2, diff, a, b, c, d)
                              : Check(pre2, pre1, diff, c, d, a, b);
        }
        return ans;
    }

    bool Check(int[][] pre1, int[][] pre2, int[] diff, int a, int b, int c, int d) {
        if (diff[a] > 0 || diff[diff.Length - 1] - diff[Math.Max(b, d) + 1] > 0) return false;
        if (d <= b) return Eq(Count(pre1, a, b), Count(pre2, a, b));
        if (b < c) {
            return diff[c] - diff[b + 1] == 0 && Eq(Count(pre1, a, b), Count(pre2, a, b)) &&
                   Eq(Count(pre1, c, d), Count(pre2, c, d));
        }
        var cnt1 = Sub(Count(pre1, a, b), Count(pre2, a, c - 1));
        var cnt2 = Sub(Count(pre2, c, d), Count(pre1, b + 1, d));
        return cnt1 != null && cnt2 != null && Eq(cnt1, cnt2);
    }

    int[] Count(int[][] pre, int i, int j) {
        int[] cnt = new int[26];
        for (int k = 0; k < 26; ++k) cnt[k] = pre[j + 1][k] - pre[i][k];
        return cnt;
    }

    int[] Sub(int[] cnt1, int[] cnt2) {
        int[] cnt = new int[26];
        for (int i = 0; i < 26; ++i) {
            cnt[i] = cnt1[i] - cnt2[i];
            if (cnt[i] < 0) return null;
        }
        return cnt;
    }

    bool Eq(int[] a, int[] b) {
        for (int i = 0; i < 26; i++) if (a[i] != b[i]) return false;
        return true;
    }
}
