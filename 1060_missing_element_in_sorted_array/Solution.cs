// LeetCode 1060 - Missing Element in Sorted Array
// https://leetcode.com/problems/missing-element-in-sorted-array/

public class Solution {
    public int MissingElement(int[] nums, int k) {
        int Missing(int i) => nums[i] - nums[0] - i;

        int n = nums.Length;
        if (k > Missing(n - 1)) {
            return nums[n - 1] + k - Missing(n - 1);
        }
        int lo = 0, hi = n - 1;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (Missing(mid) < k) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return nums[lo - 1] + k - Missing(lo - 1);
    }
}
