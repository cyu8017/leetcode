// LeetCode 2161 - Partition Array According to Given Pivot
// https://leetcode.com/problems/partition-array-according-to-given-pivot/

class Solution {
    public int[] pivotArray(int[] nums, int pivot) {
        int[] ans = new int[nums.length];
        int i = 0;
        for (int x : nums) if (x < pivot) ans[i++] = x;
        for (int x : nums) if (x == pivot) ans[i++] = x;
        for (int x : nums) if (x > pivot) ans[i++] = x;
        return ans;
    }
}
