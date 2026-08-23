// LeetCode 2465 - Number of Distinct Averages
// https://leetcode.com/problems/number-of-distinct-averages/

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

class Solution {
    public int distinctAverages(int[] nums) {
        Arrays.sort(nums);
        var seen = new HashSet<Integer>();
        int l = 0, r = nums.length - 1;
        while (l < r) {
            seen.add(nums[l] + nums[r]);
            l++;
            r--;
        }
        return seen.size();
    }
}
