// LeetCode 2256 - Minimum Average Difference
// https://leetcode.com/problems/minimum-average-difference/

class Solution {
    public int minimumAverageDifference(int[] nums) {
        int n = nums.length;
        long total = 0;
        for (int v : nums) total += v;
        long left = 0, bestDiff = Long.MAX_VALUE;
        int bestIdx = 0;
        for (int i = 0; i < n; i++) {
            left += nums[i];
            long leftAvg = left / (i + 1);
            long rightAvg = 0;
            if (i != n - 1) rightAvg = (total - left) / (n - i - 1);
            long diff = Math.abs(leftAvg - rightAvg);
            if (diff < bestDiff) { bestDiff = diff; bestIdx = i; }
        }
        return bestIdx;
    }
}
