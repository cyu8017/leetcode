// LeetCode 2163 - Minimum Difference in Sums After Removal of Elements
// https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/

public class Solution {
    public long MinimumDifference(int[] nums) {
        int n = nums.Length / 3;
        long[] left = new long[nums.Length], right = new long[nums.Length];
        var hmax = new PriorityQueue<int, int>();
        long sum = 0;
        for (int i = 0; i < n; i++) { hmax.Enqueue(nums[i], -nums[i]); sum += nums[i]; }
        left[n - 1] = sum;
        for (int i = n; i < 2 * n; i++) {
            hmax.Enqueue(nums[i], -nums[i]);
            sum += nums[i];
            sum -= hmax.Dequeue();
            left[i] = sum;
        }
        var hmin = new PriorityQueue<int, int>();
        sum = 0;
        for (int i = nums.Length - 1; i >= 2 * n; i--) { hmin.Enqueue(nums[i], nums[i]); sum += nums[i]; }
        right[2 * n] = sum;
        for (int i = 2 * n - 1; i >= n; i--) {
            hmin.Enqueue(nums[i], nums[i]);
            sum += nums[i];
            sum -= hmin.Dequeue();
            right[i] = sum;
        }
        long ans = left[n - 1] - right[n];
        for (int i = n; i < 2 * n; i++) ans = Math.Min(ans, left[i] - right[i + 1]);
        return ans;
    }
}
