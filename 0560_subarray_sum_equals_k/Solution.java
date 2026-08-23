// LeetCode 0560 - Subarray Sum Equals K
// https://leetcode.com/problems/subarray-sum-equals-k/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int subarraySum(int[] nums, int k) {
        Map<Integer, Integer> counts = new HashMap<>();
        counts.put(0, 1);
        int prefix = 0;
        int answer = 0;
        for (int num : nums) {
            prefix += num;
            answer += counts.getOrDefault(prefix - k, 0);
            counts.put(prefix, counts.getOrDefault(prefix, 0) + 1);
        }
        return answer;
    }
}
