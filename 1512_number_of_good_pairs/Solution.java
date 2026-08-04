// LeetCode 1512 - Number of Good Pairs
// https://leetcode.com/problems/number-of-good-pairs/

import java.util.*;

class Solution {
    public int numIdenticalPairs(int[] nums) {
        Map<Integer, Integer> counts = new HashMap<>();
        for (int num : nums) {
            counts.merge(num, 1, Integer::sum);
        }
        int ans = 0;
        for (int count : counts.values()) {
            ans += count * (count - 1) / 2;
        }
        return ans;
    }
}
