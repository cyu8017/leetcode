// CONFIG class=Solution method=minimumCost types=None
// LeetCode 3987 - Minimum Total Cost to Process All Elements
// https://leetcode.com/problems/minimum-total-cost-to-process-all-elements/

class Solution {
    public int minimumCost(int[] nums, int k) {
        final long mod = 1000000007L;
        long cnt = 0;
        long cur = k;
        for (int x0 : nums) {
            long x = x0;
            long diff = x - cur;
            if (diff > 0) {
                long m = (diff + k - 1) / k;
                cur += m * k;
                cnt += m;
            }
            cur -= x;
        }
        cnt %= mod;
        return (int)((cnt + 1) * cnt / 2 % mod);
    }
}
