// LeetCode 0697 - Degree of an Array
// https://leetcode.com/problems/degree-of-an-array/

import java.util.*;

class Solution {
    public int findShortestSubArray(int[] nums) {
        Map<Integer, Integer> first = new HashMap<>();
        Map<Integer, Integer> last = new HashMap<>();
        Map<Integer, Integer> count = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            first.putIfAbsent(nums[i], i);
            last.put(nums[i], i);
            count.put(nums[i], count.getOrDefault(nums[i], 0) + 1);
        }
        int degree = 0;
        for (int freq : count.values()) degree = Math.max(degree, freq);
        int best = Integer.MAX_VALUE;
        for (Map.Entry<Integer, Integer> kv : count.entrySet()) {
            if (kv.getValue() == degree) best = Math.min(best, last.get(kv.getKey()) - first.get(kv.getKey()) + 1);
        }
        return best;
    }
}
