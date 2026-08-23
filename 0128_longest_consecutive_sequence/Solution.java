// LeetCode 0128 - Longest Consecutive Sequence
// https://leetcode.com/problems/longest-consecutive-sequence/

import java.util.*;

class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> values = new HashSet<>();
        for (int num : nums) values.add(num);

        int best = 0;
        for (int num : values) {
            if (values.contains(num - 1)) continue;
            int length = 1;
            while (values.contains(num + length)) length++;
            best = Math.max(best, length);
        }
        return best;
    }
}