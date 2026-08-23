// LeetCode 2799 - Count Complete Subarrays in an Array
// https://leetcode.com/problems/count-complete-subarrays-in-an-array/

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int countCompleteSubarrays(int[] nums) {
        int need = new HashSet<Integer>(nums).size(), ans = 0, n = nums.length;
        for (int i = 0; i < n; i++) {
            var seen = new HashSet<Integer>();
            for (int j = i; j < n; j++) {
                seen.add(nums[j]);
                if (seen.size() == need) {
                    ans += n - j;
                    break;
                }
            }
        }
        return ans;
    }
}
