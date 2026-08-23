// LeetCode 2670 - Find the Distinct Difference Array
// https://leetcode.com/problems/find-the-distinct-difference-array/

import java.util.*;

class Solution {
    public int[] distinctDifferenceArray(int[] nums) {
        int n = nums.length;
        int[] suf = new int[n + 1];
        Set<Integer> seen = new HashSet<>();
        for (int i = n - 1; i >= 0; i--) {
            seen.add(nums[i]);
            suf[i] = seen.size();
        }
        seen.clear();
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) {
            seen.add(nums[i]);
            ans[i] = seen.size() - suf[i + 1];
        }
        return ans;
    }
}
