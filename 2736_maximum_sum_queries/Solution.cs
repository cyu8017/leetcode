// LeetCode 2736 - Maximum Sum Queries
// https://leetcode.com/problems/maximum-sum-queries/

using System;
using System.Collections.Generic;

public class Solution {
    public int[] MaximumSumQueries(int[] nums1, int[] nums2, int[][] queries) {
        int n = nums1.Length;
        var pts = new (int x, int y, int s)[n];
        for (int i = 0; i < n; i++) pts[i] = (nums1[i], nums2[i], nums1[i] + nums2[i]);
        Array.Sort(pts, (a, b) => b.x.CompareTo(a.x));
        var qs = new (int x, int y, int i)[queries.Length];
        for (int i = 0; i < queries.Length; i++) qs[i] = (queries[i][0], queries[i][1], i);
        Array.Sort(qs, (a, b) => b.x.CompareTo(a.x));
        var ys = new List<int>(nums2);
        foreach (var q in queries) ys.Add(q[1]);
        ys.Sort();
        int w = 0;
        for (int i = 0; i < ys.Count; i++) if (i == 0 || ys[i] != ys[i - 1]) ys[w++] = ys[i];
        ys.RemoveRange(w, ys.Count - w);
        int Rank(int y) {
            int lo = 0, hi = ys.Count;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (ys[mid] < y) lo = mid + 1;
                else hi = mid;
            }
            return lo + 1;
        }
        int m = ys.Count;
        int[] bit = new int[m + 2];
        Array.Fill(bit, -1);
        void Update(int i, int v) {
            for (; i <= m; i += i & -i) bit[i] = Math.Max(bit[i], v);
        }
        int Query(int i) {
            int best = -1;
            for (; i > 0; i -= i & -i) best = Math.Max(best, bit[i]);
            return best;
        }
        int[] ans = new int[queries.Length];
        int j = 0;
        foreach (var q in qs) {
            while (j < n && pts[j].x >= q.x) {
                Update(m - Rank(pts[j].y) + 1, pts[j].s);
                j++;
            }
            ans[q.i] = Query(m - Rank(q.y) + 1);
        }
        return ans;
    }
}
