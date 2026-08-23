// LeetCode 3073 - Maximum Increasing Triplet Value
// https://leetcode.com/problems/maximum-increasing-triplet-value/

import java.util.TreeSet;

class Solution {
    public int maximumTripletValue(int[] nums) {
        int n = nums.length;
        int[] right = new int[n];
        right[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; i--) right[i] = Math.max(nums[i], right[i + 1]);
        TreeSet<Integer> ts = new TreeSet<>();
        ts.add(nums[0]);
        int ans = 0;
        for (int j = 1; j < n - 1; j++) {
            if (right[j + 1] > nums[j]) {
                Integer it = ts.lower(nums[j]);
                if (it != null) ans = Math.max(ans, it - nums[j] + right[j + 1]);
            }
            ts.add(nums[j]);
        }
        return ans;
    }
}
