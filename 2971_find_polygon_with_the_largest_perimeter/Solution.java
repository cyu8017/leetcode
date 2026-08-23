// LeetCode 2971 - Find Polygon With the Largest Perimeter
// https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/

import java.util.Arrays;

class Solution {
    public long largestPerimeter(int[] nums) {
        Arrays.sort(nums);
        long sum = 0;
        for (int v : nums) sum += v;
        for (int i = nums.length - 1; i >= 2; i--) {
            sum -= nums[i];
            if (sum > nums[i]) return sum + nums[i];
        }
        return -1;
    }
}
