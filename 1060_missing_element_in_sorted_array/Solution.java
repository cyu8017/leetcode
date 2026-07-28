// LeetCode 1060 - Missing Element in Sorted Array
// https://leetcode.com/problems/missing-element-in-sorted-array/

class Solution {
    public int missingElement(int[] nums, int k) {
        int n = nums.length;
        if (k > missing(nums, n - 1)) {
            return nums[n - 1] + k - missing(nums, n - 1);
        }
        int lo = 0, hi = n - 1;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (missing(nums, mid) < k) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return nums[lo - 1] + k - missing(nums, lo - 1);
    }

    private int missing(int[] nums, int i) {
        return nums[i] - nums[0] - i;
    }
}
