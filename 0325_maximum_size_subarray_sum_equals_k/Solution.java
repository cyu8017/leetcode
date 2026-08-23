// LeetCode 0325 - Maximum Size Subarray Sum Equals k

// https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/



import java.util.HashMap;

import java.util.Map;



class Solution {

    public int maxSubArrayLen(int[] nums, int k) {

        Map<Integer, Integer> prefixIndex = new HashMap<>();

        prefixIndex.put(0, -1);

        int prefix = 0;

        int best = 0;

        for (int index = 0; index < nums.length; index++) {

            prefix += nums[index];

            if (prefixIndex.containsKey(prefix - k)) {

                best = Math.max(best, index - prefixIndex.get(prefix - k));

            }

            prefixIndex.putIfAbsent(prefix, index);

        }

        return best;

    }

}

