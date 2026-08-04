// LeetCode 1968 - Array With Elements Not Equal to Average of Neighbors
// https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/

import java.util.*;

class Solution {
    public int[] rearrangeArray(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length, mid = (n + 1) / 2;
        int[] ans = new int[n];
        int i = 0, j = mid, k = 0;
        while (i < mid || j < n) {
            if (i < mid) ans[k++] = nums[i++];
            if (j < n) ans[k++] = nums[j++];
        }
        return ans;
    }
}
