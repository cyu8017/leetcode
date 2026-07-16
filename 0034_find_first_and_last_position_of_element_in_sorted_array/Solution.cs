// LeetCode 0034 - Find First and Last Position of Element in Sorted Array
// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

public class Solution {
    public int[] SearchRange(int[] nums, int target) {
        if (nums.Length == 0) {
            return new int[] { -1, -1 };
        }

        int start = LowerBound(nums, target);
        if (start == nums.Length || nums[start] != target) {
            return new int[] { -1, -1 };
        }

        return new int[] { start, UpperBound(nums, target) - 1 };
    }

    private static int LowerBound(int[] nums, int target) {
        int left = 0;
        int right = nums.Length;

        while (left < right) {
            int mid = (left + right) / 2;
            if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        return left;
    }

    private static int UpperBound(int[] nums, int target) {
        int left = 0;
        int right = nums.Length;

        while (left < right) {
            int mid = (left + right) / 2;
            if (nums[mid] <= target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        return left;
    }
}
