// LeetCode 3186 - Maximum Total Damage With Spell Casting
// https://leetcode.com/problems/maximum-total-damage-with-spell-casting/

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution {
    private int[] power;
    private int[] nxt;
    private long[] f;
    private Map<Integer, Integer> cnt;
    private int n;

    public long maximumTotalDamage(int[] power) {
        n = power.length;
        Arrays.sort(power);
        this.power = power;
        cnt = new HashMap<>();
        nxt = new int[n];
        f = new long[n];
        for (int i = 0; i < n; i++) {
            cnt.merge(power[i], 1, Integer::sum);
            nxt[i] = lowerBound(power, power[i] + 3);
        }
        return dfs(0);
    }

    private long dfs(int i) {
        if (i >= n) {
            return 0;
        }
        if (f[i] != 0) {
            return f[i];
        }
        long a = dfs(i + cnt.get(power[i]));
        long b = (long) power[i] * cnt.get(power[i]) + dfs(nxt[i]);
        return f[i] = Math.max(a, b);
    }

    private static int lowerBound(int[] a, int x) {
        int lo = 0, hi = a.length;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a[mid] < x) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    }
}
