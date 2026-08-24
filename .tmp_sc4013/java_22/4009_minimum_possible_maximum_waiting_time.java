// CONFIG class=Solution method=solve types=None
// LeetCode 4009 - Minimum Possible Maximum Waiting Time
// https://leetcode.com/problems/minimum-possible-maximum-waiting-time/

import java.util.HashMap;
import java.util.Map;

class Solution {
    private int[] dem;
    private int n;
    private int W;
    private int bestServe;
    private Map<Long, Integer> memo = new HashMap<>();

    private static long packKey(int i, int f0, int f1, int d0, int d1) {
        return (((((long) i * 51 + f0) * 51 + f1) * 21 + d0) * 21 + d1);
    }

    private int maxServe(int i, int f0, int f1, int d0, int d1) {
        if (i == n) return i;
        long key = packKey(i, f0, f1, d0, d1);
        if (memo.containsKey(key)) return memo.get(key);
        int need = dem[i];
        boolean can0 = f0 >= need;
        boolean can1 = f1 >= need;
        int best = i;
        if (!can0 && !can1) {
            memo.put(key, best);
            return best;
        }
        if (can0) {
            int nd1 = d1 > d0 ? d1 - d0 : 0;
            best = Math.max(best, maxServe(i + 1, f0 - need, f1, need, nd1));
        }
        if (can1) {
            int nd0 = d0 > d1 ? d0 - d1 : 0;
            best = Math.max(best, maxServe(i + 1, f0, f1 - need, nd0, need));
        }
        memo.put(key, best);
        return best;
    }

    private boolean canWithW(int i, int f0, int f1, int d0, int d1) {
        if (i >= bestServe) return true;
        if (i == n) return true;
        long key = packKey(i, f0, f1, d0, d1);
        if (memo.containsKey(key)) return memo.get(key) == 2;
        int need = dem[i];
        boolean can0 = f0 >= need;
        boolean can1 = f1 >= need;
        boolean ok = false;
        if (!can0 && !can1) {
            memo.put(key, 1);
            return false;
        }
        if (can0 && d0 <= W) {
            int nd1 = d1 > d0 ? d1 - d0 : 0;
            if (canWithW(i + 1, f0 - need, f1, need, nd1)) ok = true;
        }
        if (!ok && can1 && d1 <= W) {
            int nd0 = d0 > d1 ? d0 - d1 : 0;
            if (canWithW(i + 1, f0, f1 - need, nd0, need)) ok = true;
        }
        memo.put(key, ok ? 2 : 1);
        return ok;
    }

    public int minMaxWaitingTime(int[] demand, int[] fuel) {
        dem = demand;
        n = demand.length;
        int f0 = fuel[0], f1 = fuel[1];
        if (f0 < demand[0] && f1 < demand[0]) return -1;
        memo.clear();
        bestServe = maxServe(0, f0, f1, 0, 0);
        if (bestServe == 0) return -1;
        int lo = 0, hi = 0;
        for (int x : demand) hi += x;
        int ans = hi;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            W = mid;
            memo.clear();
            if (canWithW(0, f0, f1, 0, 0)) {
                ans = mid;
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
        return ans;
    }
}
