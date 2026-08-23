// LeetCode 3272 - Find the Count of Good Integers
// https://leetcode.com/problems/find-the-count-of-good-integers/

using System;
using System.Collections.Generic;

public class Solution {
    string Itoa(int x) {
        if (x == 0) return "0";
        var b = new System.Text.StringBuilder();
        while (x > 0) {
            b.Insert(0, (char)('0' + x % 10));
            x /= 10;
        }
        return b.ToString();
    }

    int AtoiStr(string s) {
        int v = 0;
        foreach (char c in s) v = v * 10 + (c - '0');
        return v;
    }

    public long CountGoodIntegers(int n, int k) {
        int half = (n + 1) / 2;
        int start = 1;
        for (int i = 1; i < half; i++) start *= 10;
        int end = start * 10;
        var seen = new HashSet<string>();
        long ans = 0;
        long[] fact = new long[n + 1];
        fact[0] = 1;
        for (int i = 1; i <= n; i++) fact[i] = fact[i - 1] * i;
        for (int h = start; h < end; h++) {
            string s = Itoa(h);
            string pal = s;
            int revStart = s.Length - 1;
            if (n % 2 == 1) revStart--;
            for (int i = revStart; i >= 0; i--) pal += s[i];
            if (AtoiStr(pal) % k != 0) continue;
            char[] chars = pal.ToCharArray();
            Array.Sort(chars);
            string key = new string(chars);
            if (seen.Contains(key)) continue;
            seen.Add(key);
            int[] cnt = new int[10];
            foreach (char c in chars) cnt[c - '0']++;
            long total = fact[n];
            foreach (int c in cnt) total /= fact[c];
            if (cnt[0] > 0) {
                long bad = fact[n - 1];
                cnt[0]--;
                foreach (int c in cnt) bad /= fact[c];
                cnt[0]++;
                total -= bad;
            }
            ans += total;
        }
        return ans;
    }
}
