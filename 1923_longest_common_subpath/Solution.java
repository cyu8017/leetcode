// LeetCode 1923 - Longest Common Subpath
// https://leetcode.com/problems/longest-common-subpath/

import java.util.*;

class Solution {
    static final long BASE1 = 911382323L, MOD1 = 1_000_000_007L;
    static final long BASE2 = 972663749L, MOD2 = 1_000_000_009L;

    public int longestCommonSubpath(int n, int[][] paths) {
        int lo = 0, hi = Integer.MAX_VALUE;
        for (int[] p : paths) hi = Math.min(hi, p.length);
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (hasCommon(paths, mid)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }

    private boolean hasCommon(int[][] paths, int length) {
        if (length == 0) return true;
        Set<Long> common = null;
        long pow1 = modPow(BASE1, length, MOD1);
        long pow2 = modPow(BASE2, length, MOD2);
        for (int[] path : paths) {
            if (path.length < length) return false;
            long h1 = 0, h2 = 0;
            Set<Long> seen = new HashSet<>();
            for (int i = 0; i < path.length; i++) {
                h1 = (h1 * BASE1 + path[i] + 1) % MOD1;
                h2 = (h2 * BASE2 + path[i] + 1) % MOD2;
                if (i >= length) {
                    h1 = (h1 - (path[i - length] + 1) * pow1 % MOD1 + MOD1) % MOD1;
                    h2 = (h2 - (path[i - length] + 1) * pow2 % MOD2 + MOD2) % MOD2;
                }
                if (i >= length - 1) seen.add(h1 * MOD2 + h2);
            }
            if (common == null) common = seen;
            else {
                common.retainAll(seen);
                if (common.isEmpty()) return false;
            }
        }
        return true;
    }

    private long modPow(long a, long e, long mod) {
        long r = 1;
        while (e > 0) {
            if ((e & 1) == 1) r = r * a % mod;
            a = a * a % mod;
            e >>= 1;
        }
        return r;
    }
}
