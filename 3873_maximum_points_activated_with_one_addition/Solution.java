// LeetCode 3873 - Maximum Points Activated With One Addition
// https://leetcode.com/problems/maximum-points-activated-with-one-addition/

import java.util.HashMap;
import java.util.Map;

class Solution {
    static class UnionFind {
        Map<Long, Long> p = new HashMap<>();
        Map<Long, Integer> size = new HashMap<>();

        long find(long x) {
            if (!p.containsKey(x)) {
                p.put(x, x);
                size.put(x, 1);
            }
            if (p.get(x) != x) p.put(x, find(p.get(x)));
            return p.get(x);
        }

        boolean unite(long a, long b) {
            long pa = find(a), pb = find(b);
            if (pa == pb) return false;
            if (size.get(pa) > size.get(pb)) {
                p.put(pb, pa);
                size.put(pa, size.get(pa) + size.get(pb));
            } else {
                p.put(pa, pb);
                size.put(pb, size.get(pb) + size.get(pa));
            }
            return true;
        }
    }

    public int maxActivated(int[][] points) {
        UnionFind uf = new UnionFind();
        final long m = 3000000000L;
        for (int[] pt : points) uf.unite(pt[0], pt[1] + m);
        Map<Long, Integer> cnt = new HashMap<>();
        for (int[] pt : points) {
            long r = uf.find(pt[0]);
            cnt.put(r, cnt.getOrDefault(r, 0) + 1);
        }
        int mx1 = 0, mx2 = 0;
        for (int x : cnt.values()) {
            if (mx1 < x) { mx2 = mx1; mx1 = x; }
            else if (mx2 < x) mx2 = x;
        }
        return mx1 + mx2 + 1;
    }
}
