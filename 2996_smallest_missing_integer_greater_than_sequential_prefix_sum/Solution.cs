// LeetCode 2996 - Smallest Missing Integer Greater Than Sequential Prefix Sum
// https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/

using System.Collections.Generic;

public class Solution {
    public int MissingInteger(int[] nums) {
        int sum = nums[0];
        for (int i = 1; i < nums.Length && nums[i] == nums[i - 1] + 1; i++) {
            sum += nums[i];
        }
        var seen = new HashSet<int>(nums);
        while (seen.Contains(sum)) sum++;
        return sum;
    }
}
