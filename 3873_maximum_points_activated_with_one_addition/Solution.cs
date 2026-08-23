// LeetCode 3873 - Maximum Points Activated With One Addition
// https://leetcode.com/problems/maximum-points-activated-with-one-addition/

using System.Collections.Generic;

public class Solution {
    class UnionFind {
        Dictionary<long, long> p = new Dictionary<long, long>();
        Dictionary<long, int> size = new Dictionary<long, int>();
        public long Find(long x) {
            if (!p.ContainsKey(x)) {
                p[x] = x;
                size[x] = 1;
            }
            if (p[x] != x) p[x] = Find(p[x]);
            return p[x];
        }
        public bool Unite(long a, long b) {
            long pa = Find(a), pb = Find(b);
            if (pa == pb) return false;
            if (size[pa] > size[pb]) {
                p[pb] = pa;
                size[pa] += size[pb];
            } else {
                p[pa] = pb;
                size[pb] += size[pa];
            }
            return true;
        }
    }

    public int MaxActivated(int[][] points) {
        var uf = new UnionFind();
        const long m = 3000000000L;
        foreach (var pt in points) uf.Unite(pt[0], pt[1] + m);
        var cnt = new Dictionary<long, int>();
        foreach (var pt in points) {
            long r = uf.Find(pt[0]);
            if (!cnt.ContainsKey(r)) cnt[r] = 0;
            cnt[r]++;
        }
        int mx1 = 0, mx2 = 0;
        foreach (var x in cnt.Values) {
            if (mx1 < x) { mx2 = mx1; mx1 = x; }
            else if (mx2 < x) mx2 = x;
        }
        return mx1 + mx2 + 1;
    }
}
