// LeetCode 3960 - Frequency Balance Subarray
// https://leetcode.com/problems/frequency-balance-subarray/

using System;
using System.Collections.Generic;

public class Solution {
    public int GetLength(int[] nums) {
        int n = nums.Length;
        int ans = 1;
        for (int l = 0; l < n; l++) {
            var cnt = new Dictionary<int, int>();
            var freq = new Dictionary<int, int>();
            for (int r = l; r < n; r++) {
                int x = nums[r];
                int c = cnt.TryGetValue(x, out int cv) ? cv : 0;
                if (freq.TryGetValue(c, out int fc) && fc > 0) {
                    if (--freq[c] == 0) freq.Remove(c);
                }
                cnt[x] = c + 1;
                if (!freq.ContainsKey(cnt[x])) freq[cnt[x]] = 0;
                freq[cnt[x]]++;
                int cx = cnt[x];
                if (cnt.Count == 1 || (freq.Count == 2 && ((freq.TryGetValue(cx * 2, out int f2) && f2 > 0) || (cx % 2 == 0 && freq.TryGetValue(cx / 2, out int f3) && f3 > 0)))) {
                    ans = Math.Max(ans, r - l + 1);
                }
            }
        }
        return ans;
    }
}
