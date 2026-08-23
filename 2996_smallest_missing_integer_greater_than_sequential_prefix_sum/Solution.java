// LeetCode 2996 - Smallest Missing Integer Greater Than Sequential Prefix Sum
// https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int missingInteger(int[] nums) {
        int sum = nums[0];
        for (int i = 1; i < nums.length && nums[i] == nums[i - 1] + 1; i++) {
            sum += nums[i];
        }
        Set<Integer> seen = new HashSet<>();
        for (int v : nums) seen.add(v);
        while (seen.contains(sum)) sum++;
        return sum;
    }
}
