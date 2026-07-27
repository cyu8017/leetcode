// LeetCode 1681 - Minimum Incompatibility
// https://leetcode.com/problems/minimum-incompatibility/

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution {
    private int n;
    private int full;
    private Map<Integer, Integer> groups;
    private int[] memo;

    public int minimumIncompatibility(int[] nums, int k) {
        n = nums.length;
        int size = n / k;
        full = (1 << n) - 1;
        groups = new HashMap<>();
        for (int mask = 0; mask <= full; mask++) {
            if (Integer.bitCount(mask) != size) {
                continue;
            }
            int[] vals = new int[size];
            int idx = 0;
            boolean ok = true;
            boolean[] used = new boolean[17];
            int mn = Integer.MAX_VALUE;
            int mx = Integer.MIN_VALUE;
            for (int i = 0; i < n; i++) {
                if (((mask >> i) & 1) == 1) {
                    int v = nums[i];
                    if (used[v]) {
                        ok = false;
                        break;
                    }
                    used[v] = true;
                    vals[idx++] = v;
                    mn = Math.min(mn, v);
                    mx = Math.max(mx, v);
                }
            }
            if (ok) {
                groups.put(mask, mx - mn);
            }
        }
        memo = new int[1 << n];
        Arrays.fill(memo, -2);
        int ans = dp(0);
        return ans >= 1_000_000_000 ? -1 : ans;
    }

    private int dp(int mask) {
        if (mask == full) {
            return 0;
        }
        if (memo[mask] != -2) {
            return memo[mask];
        }
        int first = 0;
        while (((mask >> first) & 1) == 1) {
            first++;
        }
        int best = 1_000_000_000;
        for (Map.Entry<Integer, Integer> e : groups.entrySet()) {
            int g = e.getKey();
            if (((g >> first) & 1) == 1 && (g & mask) == 0) {
                best = Math.min(best, e.getValue() + dp(mask | g));
            }
        }
        memo[mask] = best;
        return best;
    }
}
