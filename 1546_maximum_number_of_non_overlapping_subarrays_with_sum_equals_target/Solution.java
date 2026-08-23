// LeetCode 1546 - Maximum Number of Non-Overlapping Subarrays With Sum Equals Target
// https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/

import java.util.*;

class Solution {
    public int maxNonOverlapping(int[] nums, int target) {
        Set<Integer> seen = new HashSet<>();
        seen.add(0);
        int prefix = 0, answer = 0;
        for (int value : nums) {
            prefix += value;
            if (seen.contains(prefix - target)) {
                answer++;
                prefix = 0;
                seen.clear();
                seen.add(0);
            } else {
                seen.add(prefix);
            }
        }
        return answer;
    }
}
