// LeetCode 0215 - Kth Largest Element in an Array
// https://leetcode.com/problems/kth-largest-element-in-an-array/

public class Solution {
    private static readonly Random Random = new();

    public int FindKthLargest(int[] nums, int k) {
        var target = nums.Length - k;
        var left = 0;
        var right = nums.Length - 1;
        while (left <= right) {
            var pivotIndex = Partition(nums, left, right);
            if (pivotIndex == target) {
                return nums[pivotIndex];
            }
            if (pivotIndex < target) {
                left = pivotIndex + 1;
            } else {
                right = pivotIndex - 1;
            }
        }
        return nums[left];
    }

    private static int Partition(int[] nums, int left, int right) {
        var pivotIndex = left + Random.Next(right - left + 1);
        Swap(nums, pivotIndex, right);
        var store = left;
        for (var i = left; i < right; i++) {
            if (nums[i] <= nums[right]) {
                Swap(nums, store, i);
                store++;
            }
        }
        Swap(nums, store, right);
        return store;
    }

    private static void Swap(int[] nums, int i, int j) {
        (nums[i], nums[j]) = (nums[j], nums[i]);
    }
}
