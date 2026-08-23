// LeetCode 2875 - Minimum Size Subarray in Infinite Array
// https://leetcode.com/problems/minimum-size-subarray-in-infinite-array/

class Solution {
    public int minSizeSubarray(int[] nums, int target) {
        int n = nums.length;
        long total = 0;
        for (int v : nums) total += v;
        int ans = 1 << 30;
        if (total > 0) {
            int loops = (int) (target / total);
            int remain = (int) (target % total);
            if (remain == 0) return loops * n;
            int[] arr = new int[2 * n];
            System.arraycopy(nums, 0, arr, 0, n);
            System.arraycopy(nums, 0, arr, n, n);
            int left = 0, sum = 0, best = 1 << 30;
            for (int right = 0; right < arr.length; right++) {
                sum += arr[right];
                while (sum > remain && left <= right) {
                    sum -= arr[left];
                    left++;
                }
                if (sum == remain && right - left + 1 < best) best = right - left + 1;
            }
            if (best < (1 << 30)) ans = loops * n + best;
        }
        return ans == (1 << 30) ? -1 : ans;
    }
}
