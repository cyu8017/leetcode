// LeetCode 3154 - Find Number of Ways to Reach the K-th Stair
// https://leetcode.com/problems/find-number-of-ways-to-reach-the-k-th-stair/

using System.Collections.Generic;

public class Solution {
    public int WaysToReachStair(int k) {
        var f = new Dictionary<long, int>();
        int Dfs(long i, int j, int jump) {
            if (i > k + 1) return 0;
            long key = (i << 32) | ((long)jump << 1) | (uint)j;
            if (f.TryGetValue(key, out int cached)) return cached;
            int ans = 0;
            if (i == k) ans++;
            if (i > 0 && j == 0) ans += Dfs(i - 1, 1, jump);
            ans += Dfs(i + (1L << jump), 0, jump + 1);
            return f[key] = ans;
        }
        return Dfs(1, 0, 0);
    }
}
