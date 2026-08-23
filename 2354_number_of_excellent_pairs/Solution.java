// LeetCode 2354 - Number of Excellent Pairs
// https://leetcode.com/problems/number-of-excellent-pairs/

import java.util.HashSet;
import java.util.Set;

class Solution {
    public long countExcellentPairs(int[] nums, int k) {
        Set<Integer> uniq = new HashSet<>();
        for (int x : nums) uniq.add(x);
        int[] cnt = new int[32];
        for (int x : uniq) {
            int bits = Integer.bitCount(x);
            cnt[bits]++;
        }
        long ans = 0;
        for (int i = 0; i < 32; i++) {
            for (int j = 0; j < 32; j++) {
                if (i + j >= k) ans += (long) cnt[i] * cnt[j];
            }
        }
        return ans;
    }
}
