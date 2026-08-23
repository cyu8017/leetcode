// LeetCode 3811 - Number Of Alternating Xor Partitions
// https://leetcode.com/problems/number_of_alternating_xor_partitions/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int alternatingXOR(int[] nums, int target1, int target2) {
        final int MOD = 1_000_000_007;
        Map<Integer, Integer> cnt1 = new HashMap<>();
        Map<Integer, Integer> cnt2 = new HashMap<>();
        cnt2.put(0, 1);
        int pre = 0, ans = 0;
        for (int x : nums) {
            pre ^= x;
            int a = cnt2.getOrDefault(pre ^ target1, 0);
            int b = cnt1.getOrDefault(pre ^ target2, 0);
            ans = (a + b) % MOD;
            cnt1.merge(pre, a, (x1, y1) -> (x1 + y1) % MOD);
            cnt2.merge(pre, b, (x1, y1) -> (x1 + y1) % MOD);
        }
        return ans;
    }
}
