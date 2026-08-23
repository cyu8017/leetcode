// LeetCode 3859 - Count Subarrays With K Distinct Integers
// https://leetcode.com/problems/count-subarrays-with-k-distinct-integers/

using System.Collections.Generic;

public class Solution {
    public long CountSubarrays(int[] nums, int k, int m) {
        long F(int lim) {
            var cnt = new Dictionary<int, int>();
            long ans = 0;
            int l = 0, t = 0;
            foreach (int x in nums) {
                if (!cnt.ContainsKey(x)) cnt[x] = 0;
                if (++cnt[x] == m) t++;
                while (cnt.Count >= lim && t >= k) {
                    int y = nums[l++];
                    if (--cnt[y] == m - 1) t--;
                    if (cnt[y] == 0) cnt.Remove(y);
                }
                ans += l;
            }
            return ans;
        }
        return F(k) - F(k + 1);
    }
}
