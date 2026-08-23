// LeetCode 2903 - Find Indices With Index and Value Difference I
// https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/

class Solution {
    public int[] findIndices(int[] nums, int indexDifference, int valueDifference) {
        int n = nums.length;
        for (int i = 0; i < n; i++)
            for (int j = i; j < n; j++) {
                int di = Math.abs(j - i), dv = Math.abs(nums[i] - nums[j]);
                if (di >= indexDifference && dv >= valueDifference) return new int[] {i, j};
            }
        return new int[] {-1, -1};
    }
}
