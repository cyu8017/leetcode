// LeetCode 1679 - Max Number of K-Sum Pairs
// https://leetcode.com/problems/max-number-of-k-sum-pairs/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int maxOperations(int[] nums, int k) {
        Map<Integer, Integer> count = new HashMap<>();
        int ans = 0;
        for (int x : nums) {
            int need = k - x;
            int have = count.getOrDefault(need, 0);
            if (have > 0) {
                count.put(need, have - 1);
                ans++;
            } else {
                count.merge(x, 1, Integer::sum);
            }
        }
        return ans;
    }
}
