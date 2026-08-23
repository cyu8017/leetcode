// LeetCode 2013 - Detect Squares
// https://leetcode.com/problems/detect-squares/

import java.util.*;

class DetectSquares {
    private final Map<Long, Integer> cnt = new HashMap<>();

    public DetectSquares() {}

    private long key(int x, int y) {
        return (((long) x) << 32) ^ (y & 0xffffffffL);
    }

    public void add(int[] point) {
        cnt.merge(key(point[0], point[1]), 1, Integer::sum);
    }

    public int count(int[] point) {
        int x = point[0], y = point[1], ans = 0;
        for (Map.Entry<Long, Integer> kv : cnt.entrySet()) {
            long k = kv.getKey();
            int px = (int) (k >> 32), py = (int) k, c = kv.getValue();
            if (px == x || py == y) continue;
            if (Math.abs(px - x) != Math.abs(py - y)) continue;
            int c1 = cnt.getOrDefault(key(px, y), 0);
            int c2 = cnt.getOrDefault(key(x, py), 0);
            ans += c * c1 * c2;
        }
        return ans;
    }
}
