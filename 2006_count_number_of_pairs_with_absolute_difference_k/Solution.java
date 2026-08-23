// LeetCode 2006 - Count Number of Pairs With Absolute Difference K
// https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/

import java.util.*;

class Solution {
    public int countKDifference(int[] nums, int k) {
        Map<Integer, Integer> freq = new HashMap<>();
        int ans = 0;
        for (int x : nums) {
            ans += freq.getOrDefault(x - k, 0);
            ans += freq.getOrDefault(x + k, 0);
            freq.merge(x, 1, Integer::sum);
        }
        return ans;
    }
}
