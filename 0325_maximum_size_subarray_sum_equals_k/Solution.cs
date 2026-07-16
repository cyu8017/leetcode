// LeetCode 0325 - Maximum Size Subarray Sum Equals k

// https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/



using System.Collections.Generic;



public class Solution {

    public int MaxSubArrayLen(int[] nums, int k) {

        Dictionary<int, int> prefixIndex = new() { [0] = -1 };

        int prefix = 0;

        int best = 0;

        for (int index = 0; index < nums.Length; index++) {

            prefix += nums[index];

            if (prefixIndex.TryGetValue(prefix - k, out int start)) {

                best = System.Math.Max(best, index - start);

            }

            prefixIndex.TryAdd(prefix, index);

        }

        return best;

    }

}

