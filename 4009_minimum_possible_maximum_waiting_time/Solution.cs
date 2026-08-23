// LeetCode 4009 - Minimum Possible Maximum Waiting Time
// https://leetcode.com/problems/minimum-possible-maximum-waiting-time/

using System.Collections.Generic;

public class Solution {
    int[] dem;
    int n;
    int W;
    int bestServe;
    Dictionary<long, int> memo = new Dictionary<long, int>();

    static long PackKey(int i, int f0, int f1, int d0, int d1) {
        return (((((long)i * 51 + f0) * 51 + f1) * 21 + d0) * 21 + d1);
    }

    int MaxServe(int i, int f0, int f1, int d0, int d1) {
        if (i == n) return i;
        long key = PackKey(i, f0, f1, d0, d1);
        if (memo.TryGetValue(key, out int cached)) return cached;
        int need = dem[i];
        bool can0 = f0 >= need;
        bool can1 = f1 >= need;
        int best = i;
        if (!can0 && !can1) {
            memo[key] = best;
            return best;
        }
        if (can0) {
            int nd1 = d1 > d0 ? d1 - d0 : 0;
            int v = MaxServe(i + 1, f0 - need, f1, need, nd1);
            if (v > best) best = v;
        }
        if (can1) {
            int nd0 = d0 > d1 ? d0 - d1 : 0;
            int v = MaxServe(i + 1, f0, f1 - need, nd0, need);
            if (v > best) best = v;
        }
        memo[key] = best;
        return best;
    }

    bool CanWithW(int i, int f0, int f1, int d0, int d1) {
        if (i >= bestServe) return true;
        if (i == n) return true;
        long key = PackKey(i, f0, f1, d0, d1);
        if (memo.TryGetValue(key, out int cached)) return cached == 2;
        int need = dem[i];
        bool can0 = f0 >= need;
        bool can1 = f1 >= need;
        bool ok = false;
        if (!can0 && !can1) {
            memo[key] = 1;
            return false;
        }
        if (can0 && d0 <= W) {
            int nd1 = d1 > d0 ? d1 - d0 : 0;
            if (CanWithW(i + 1, f0 - need, f1, need, nd1)) ok = true;
        }
        if (!ok && can1 && d1 <= W) {
            int nd0 = d0 > d1 ? d0 - d1 : 0;
            if (CanWithW(i + 1, f0, f1 - need, nd0, need)) ok = true;
        }
        memo[key] = ok ? 2 : 1;
        return ok;
    }

    public int MinMaxWaitingTime(int[] demand, int[] fuel) {
        dem = demand;
        n = demand.Length;
        int f0 = fuel[0], f1 = fuel[1];
        if (f0 < demand[0] && f1 < demand[0]) return -1;
        memo.Clear();
        bestServe = MaxServe(0, f0, f1, 0, 0);
        if (bestServe == 0) return -1;
        int lo = 0, hi = 0;
        foreach (int x in demand) hi += x;
        int ans = hi;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            W = mid;
            memo.Clear();
            if (CanWithW(0, f0, f1, 0, 0)) {
                ans = mid;
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
        return ans;
    }
}
