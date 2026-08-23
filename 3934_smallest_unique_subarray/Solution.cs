// LeetCode 3934 - Smallest Unique Subarray
// https://leetcode.com/problems/smallest-unique-subarray/

using System;

public class Solution {
    public int SmallestUniqueSubarray(int[] nums) {
        int n = nums.Length;
        int[] sa = new int[n], rank = (int[])nums.Clone();
        for (int i = 0; i < n; i++) sa[i] = i;
        for (int width = 1; width < n; width <<= 1) {
            Array.Sort(sa, (a, b) => {
                if (rank[a] != rank[b]) return rank[a].CompareTo(rank[b]);
                int ra = a + width < n ? rank[a + width] : -1;
                int rb = b + width < n ? rank[b + width] : -1;
                return ra.CompareTo(rb);
            });
            int[] next = new int[n];
            for (int i = 1; i < n; i++) {
                int a = sa[i - 1], b = sa[i];
                bool different = rank[a] != rank[b];
                int ra = a + width < n ? rank[a + width] : -1;
                int rb = b + width < n ? rank[b + width] : -1;
                next[b] = (different || ra != rb) ? next[a] + 1 : next[a];
            }
            rank = next;
            if (rank[sa[n - 1]] == n - 1) break;
        }
        int[] pos = new int[n];
        for (int i = 0; i < n; i++) pos[sa[i]] = i;
        int[] lcp = new int[Math.Max(0, n - 1)];
        int height = 0;
        for (int i = 0; i < n; i++) {
            int p = pos[i];
            if (p == n - 1) {
                height = 0;
                continue;
            }
            int j = sa[p + 1];
            while (i + height < n && j + height < n && nums[i + height] == nums[j + height]) height++;
            lcp[p] = height;
            if (height > 0) height--;
        }
        int ans = n;
        for (int p = 0; p < n; p++) {
            int start = sa[p];
            int need = 1;
            if (p > 0 && lcp[p - 1] + 1 > need) need = lcp[p - 1] + 1;
            if (p + 1 < n && lcp[p] + 1 > need) need = lcp[p] + 1;
            if (need <= n - start && need < ans) ans = need;
        }
        return ans;
    }
}
