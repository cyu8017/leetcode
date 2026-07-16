// LeetCode 0493 - Reverse Pairs
// https://leetcode.com/problems/reverse-pairs/

public class Solution {
    public int ReversePairs(int[] nums) {
        return MergeSort(nums, 0, nums.Length - 1);
    }

    private static int MergeSort(int[] nums, int start, int end) {
        if (start >= end) {
            return 0;
        }
        int mid = (start + end) / 2;
        int count = MergeSort(nums, start, mid) + MergeSort(nums, mid + 1, end);
        int j = mid + 1;
        for (int i = start; i <= mid; i++) {
            while (j <= end && nums[i] > 2L * nums[j]) {
                j++;
            }
            count += j - (mid + 1);
        }
        int[] slice = new int[end - start + 1];
        Array.Copy(nums, start, slice, 0, slice.Length);
        Array.Sort(slice);
        Array.Copy(slice, 0, nums, start, slice.Length);
        return count;
    }
}
