// LeetCode 3086 - Minimum Moves to Pick K Ones
// https://leetcode.com/problems/minimum-moves-to-pick-k-ones/

using System;

public class Solution {
    public long MinimumMoves(int[] nums, int k, int maxChanges) {
        int n = nums.Length;
        int[] cnt = new int[n + 1], s = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            cnt[i] = cnt[i - 1] + nums[i - 1];
            s[i] = s[i - 1] + i * nums[i - 1];
        }
        long ans = long.MaxValue;
        for (int i = 1; i <= n; i++) {
            long t = 0;
            int need = k - nums[i - 1];
            foreach (int j in new[] { i - 1, i + 1 }) {
                if (need > 0 && 1 <= j && j <= n && nums[j - 1] == 1) {
                    need--;
                    t++;
                }
            }
            int c = Math.Min(need, maxChanges);
            need -= c;
            t += c * 2L;
            if (need <= 0) {
                ans = Math.Min(ans, t);
                continue;
            }
            int l = 2, r = Math.Max(i - 1, n - i);
            while (l <= r) {
                int mid = (l + r) >> 1;
                int l1 = Math.Max(1, i - mid), r1 = Math.Max(0, i - 2);
                int l2 = Math.Min(n + 1, i + 2), r2 = Math.Min(n, i + mid);
                int c1 = cnt[r1] - cnt[l1 - 1];
                int c2 = cnt[r2] - cnt[l2 - 1];
                if (c1 + c2 >= need) {
                    long t1 = (long)c1 * i - (s[r1] - s[l1 - 1]);
                    long t2 = s[r2] - s[l2 - 1] - (long)c2 * i;
                    ans = Math.Min(ans, t + t1 + t2);
                    r = mid - 1;
                } else {
                    l = mid + 1;
                }
            }
        }
        return ans;
    }
}
