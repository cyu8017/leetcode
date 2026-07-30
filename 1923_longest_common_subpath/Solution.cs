// LeetCode 1923 - Longest Common Subpath
// https://leetcode.com/problems/longest-common-subpath/

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int LongestCommonSubpath(int n, int[][] paths) {
        const long BASE1 = 911382323, MOD1 = 1000000007;
        const long BASE2 = 972663749, MOD2 = 1000000009;

        bool HasCommon(int length) {
            if (length == 0) return true;
            HashSet<(long, long)> common = null;
            long pow1 = 1, pow2 = 1;
            for (int i = 0; i < length; i++) {
                pow1 = pow1 * BASE1 % MOD1;
                pow2 = pow2 * BASE2 % MOD2;
            }
            foreach (var path in paths) {
                if (path.Length < length) return false;
                long h1 = 0, h2 = 0;
                var seen = new HashSet<(long, long)>();
                for (int i = 0; i < path.Length; i++) {
                    h1 = (h1 * BASE1 + path[i] + 1) % MOD1;
                    h2 = (h2 * BASE2 + path[i] + 1) % MOD2;
                    if (i >= length) {
                        h1 = (h1 - (path[i - length] + 1) * pow1 % MOD1 + MOD1) % MOD1;
                        h2 = (h2 - (path[i - length] + 1) * pow2 % MOD2 + MOD2) % MOD2;
                    }
                    if (i >= length - 1) seen.Add((h1, h2));
                }
                if (common == null) common = seen;
                else {
                    common.IntersectWith(seen);
                    if (common.Count == 0) return false;
                }
            }
            return true;
        }

        int lo = 0, hi = paths.Min(p => p.Length);
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (HasCommon(mid)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }
}