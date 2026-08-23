// LeetCode 2229 - Check if an Array Is Consecutive
// https://leetcode.com/problems/check-if-an-array-is-consecutive/

import java.util.HashSet;
import java.util.Set;

class Solution {
    public boolean isConsecutive(int[] nums) {
        int mn = nums[0], mx = nums[0];
        var seen = new HashSet<Integer>();
        for (int x : nums) {
            if (!seen.add(x)) return false;
            mn = Math.min(mn, x);
            mx = Math.max(mx, x);
        }
        return mx - mn + 1 == nums.length;
    }
}
