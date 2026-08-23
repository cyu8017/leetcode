// LeetCode 3810 - Minimum Operations To Reach Target Array
// https://leetcode.com/problems/minimum-operations-to-reach-target-array/

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int minOperations(int[] nums, int[] target) {
        var s = new HashSet<Integer>();
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != target[i]) s.add(nums[i]);
        }
        return s.size();
    }
}
