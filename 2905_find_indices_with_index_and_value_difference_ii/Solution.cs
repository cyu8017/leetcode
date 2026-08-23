// LeetCode 2905 - Find Indices With Index and Value Difference II
// https://leetcode.com/problems/find-indices-with-index-and-value-difference-ii/

public class Solution {
    public int[] FindIndices(int[] nums, int indexDifference, int valueDifference) {
        int n = nums.Length;
        int minIdx = 0, maxIdx = 0;
        for (int j = indexDifference; j < n; j++) {
            int i = j - indexDifference;
            if (nums[i] < nums[minIdx]) minIdx = i;
            if (nums[i] > nums[maxIdx]) maxIdx = i;
            if (nums[j] - nums[minIdx] >= valueDifference) return new[] { minIdx, j };
            if (nums[maxIdx] - nums[j] >= valueDifference) return new[] { maxIdx, j };
        }
        return new[] { -1, -1 };
    }
}
