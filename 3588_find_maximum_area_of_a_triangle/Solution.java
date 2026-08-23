// LeetCode 3588 - Find Maximum Area of a Triangle
// https://leetcode.com/problems/find-maximum-area-of-a-triangle/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public long maxArea(int[][] coords) {
        long ans = calc(coords);
        for (int[] c : coords) {
            int t = c[0];
            c[0] = c[1];
            c[1] = t;
        }
        ans = Math.max(ans, calc(coords));
        return ans > 0 ? ans : -1;
    }

    long calc(int[][] coords) {
        int mn = (int) 1e9, mx = 0;
        Map<Integer, Integer> f = new HashMap<>();
        Map<Integer, Integer> g = new HashMap<>();
        for (int[] c : coords) {
            int x = c[0], y = c[1];
            mn = Math.min(mn, x);
            mx = Math.max(mx, x);
            if (f.containsKey(x)) {
                f.put(x, Math.min(f.get(x), y));
                g.put(x, Math.max(g.get(x), y));
            } else {
                f.put(x, y);
                g.put(x, y);
            }
        }
        long ans = 0;
        for (Map.Entry<Integer, Integer> e : f.entrySet()) {
            int x = e.getKey(), y = e.getValue();
            int d = g.get(x) - y;
            ans = Math.max(ans, 1L * d * Math.max(mx - x, x - mn));
        }
        return ans;
    }
}
