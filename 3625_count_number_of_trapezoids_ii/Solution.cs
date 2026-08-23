// LeetCode 3625 - Count Number of Trapezoids II
// https://leetcode.com/problems/count-number-of-trapezoids-ii/

using System.Collections.Generic;

public class Solution {
    public int CountTrapezoids(int[][] points) {
        int n = points.Length;
        var cnt1 = new Dictionary<double, Dictionary<double, int>>();
        var cnt2 = new Dictionary<int, Dictionary<double, int>>();
        for (int i = 0; i < n; i++) {
            int x1 = points[i][0], y1 = points[i][1];
            for (int j = 0; j < i; j++) {
                int x2 = points[j][0], y2 = points[j][1];
                int dx = x2 - x1, dy = y2 - y1;
                double k, b;
                if (dx == 0) {
                    k = 1e9;
                    b = x1;
                } else {
                    k = (double)dy / dx;
                    b = (double)((long)y1 * dx - (long)x1 * dy) / dx;
                }
                if (!cnt1.ContainsKey(k)) cnt1[k] = new Dictionary<double, int>();
                if (!cnt1[k].ContainsKey(b)) cnt1[k][b] = 0;
                cnt1[k][b]++;
                int p = (x1 + x2 + 2000) * 4000 + (y1 + y2 + 2000);
                if (!cnt2.ContainsKey(p)) cnt2[p] = new Dictionary<double, int>();
                if (!cnt2[p].ContainsKey(k)) cnt2[p][k] = 0;
                cnt2[p][k]++;
            }
        }
        int ans = 0;
        foreach (var e in cnt1.Values) {
            int s = 0;
            foreach (var t in e.Values) {
                ans += s * t;
                s += t;
            }
        }
        foreach (var e in cnt2.Values) {
            int s = 0;
            foreach (var t in e.Values) {
                ans -= s * t;
                s += t;
            }
        }
        return ans;
    }
}
