// LeetCode 2967 - Minimum Cost to Make Array Equalindromic
// https://leetcode.com/problems/minimum-cost-to-make-array-equalindromic/

using System;
using System.Collections.Generic;

public class Solution {
    public long MinimumCost(int[] nums) {
        Array.Sort(nums);
        int n = nums.Length;
        int median = nums[n / 2];
        int MakePal(int x) {
            char[] ch = x.ToString().ToCharArray();
            for (int i = 0, j = ch.Length - 1; i < j; i++, j--) ch[j] = ch[i];
            return int.Parse(new string(ch));
        }
        var candidates = new List<int>();
        candidates.Add(MakePal(median));
        string s = median.ToString();
        int half = int.Parse(s.Substring(0, (s.Length + 1) / 2));
        for (int d = -2; d <= 2; d++) {
            int h = half + d;
            if (h <= 0) continue;
            string hs = h.ToString();
            string pal;
            if (s.Length % 2 == 0) {
                char[] rb = hs.ToCharArray();
                Array.Reverse(rb);
                pal = hs + new string(rb);
            } else {
                char[] rb = hs.Substring(0, hs.Length - 1).ToCharArray();
                Array.Reverse(rb);
                pal = hs + new string(rb);
            }
            if (int.TryParse(pal, out int pv)) candidates.Add(pv);
        }
        foreach (int v in new int[] { 1, 9, 11, 99, 101 }) candidates.Add(v);
        long Cost(int p) {
            long c = 0;
            foreach (int v in nums) c += Math.Abs((long)v - p);
            return c;
        }
        long ans = long.MaxValue / 4;
        foreach (int p in candidates) {
            if (p <= 0) continue;
            ans = Math.Min(ans, Cost(p));
        }
        return ans;
    }
}
