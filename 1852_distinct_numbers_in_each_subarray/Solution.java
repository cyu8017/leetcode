// LeetCode 1852 - Distinct Numbers in Each Subarray
// https://leetcode.com/problems/distinct-numbers-in-each-subarray/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] distinctNumbers(int[] nums, int k) {
        Map<Integer, Integer> counts = new HashMap<>();
        for (int i = 0; i < k; i++) {
            counts.merge(nums[i], 1, Integer::sum);
        }

        int[] result = new int[nums.length - k + 1];
        result[0] = counts.size();
        int left = 0;

        for (int right = k; right < nums.length; right++) {
            counts.merge(nums[right], 1, Integer::sum);
            int outgoing = nums[left];
            counts.merge(outgoing, -1, Integer::sum);
            if (counts.get(outgoing) == 0) {
                counts.remove(outgoing);
            }
            left++;
            result[left] = counts.size();
        }

        return result;
    }
}
