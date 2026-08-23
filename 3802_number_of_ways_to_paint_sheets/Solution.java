// LeetCode 3802 - Number Of Ways To Paint Sheets
// https://leetcode.com/problems/number_of_ways_to_paint_sheets/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public int numberOfWays(int n, int[] limit) {
        final long MOD = 1_000_000_007;
        Arrays.sort(limit);
        List<Integer> points = new ArrayList<>();
        points.add(1);
        points.add(n);
        for (int x : limit) {
            if (x + 1 > 1 && x + 1 < n) points.add(x + 1);
            if (n - x > 1 && n - x < n) points.add(n - x);
        }
        points.sort(null);
        int u = 0;
        for (int i = 0; i < points.size(); i++) {
            if (u == 0 || !points.get(i).equals(points.get(u - 1))) {
                points.set(u++, points.get(i));
            }
        }
        points = points.subList(0, u);
        long ans = 0;
        for (int i = 0; i + 1 < points.size(); i++) {
            int x = points.get(i);
            long a = countGE(limit, x), b = countGE(limit, n - x);
            long same = countGE(limit, Math.max(x, n - x));
            long ways = (a * b - same) % MOD;
            long length = points.get(i + 1) - x;
            ans = (ans + ways * length) % MOD;
        }
        if (ans < 0) ans += MOD;
        return (int) ans;
    }

    private long countGE(int[] limit, int x) {
        int lo = 0, hi = limit.length;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (limit[mid] < x) lo = mid + 1;
            else hi = mid;
        }
        return limit.length - lo;
    }
}
