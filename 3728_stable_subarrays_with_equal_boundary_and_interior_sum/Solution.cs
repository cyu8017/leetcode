// LeetCode 3728 - Stable Subarrays With Equal Boundary and Interior Sum
// https://leetcode.com/problems/stable-subarrays-with-equal-boundary-and-interior-sum/

using System.Collections.Generic;

public class Solution {
    public long CountStableSubarrays(int[] capacity) {
        int n = capacity.Length;
        long[] s = new long[n + 1];
        for (int i = 1; i <= n; i++) s[i] = s[i - 1] + capacity[i - 1];
        var cnt = new Dictionary<(int, long), int>();
        long ans = 0;
        for (int r = 2; r < n; r++) {
            int l = r - 2;
            var keyL = (capacity[l], (long)capacity[l] + s[l + 1]);
            if (!cnt.ContainsKey(keyL)) cnt[keyL] = 0;
            cnt[keyL]++;
            var keyR = (capacity[r], s[r]);
            if (cnt.ContainsKey(keyR)) ans += cnt[keyR];
        }
        return ans;
    }
}
