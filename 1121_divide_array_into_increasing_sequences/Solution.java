// LeetCode 1121 - Divide Array Into Increasing Sequences
// https://leetcode.com/problems/divide-array-into-increasing-sequences/

import java.util.*;

class Solution {
    public boolean canDivideIntoSubsequences(int[] nums, int k) {
        Map<Integer, Integer> count = new HashMap<>();
        int maxFreq = 0;
        for (int x : nums) {
            int c = count.merge(x, 1, Integer::sum);
            maxFreq = Math.max(maxFreq, c);
        }
        return nums.length >= (long) k * maxFreq;
    }
}
