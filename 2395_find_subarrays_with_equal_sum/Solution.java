// LeetCode 2395 - Find Subarrays With Equal Sum
// https://leetcode.com/problems/find-subarrays-with-equal-sum/

import java.util.HashSet;
import java.util.Set;

class Solution {
    public boolean findSubarrays(int[] nums) {
        var seen = new HashSet<>();
        for (int i = 0; i + 1 < nums.length; i++) {
            int s = nums[i] + nums[i + 1];
            if (seen.contains(s)) return true;
            seen.add(s);
        }
        return false;
    }
}
