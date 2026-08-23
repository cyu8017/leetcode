// LeetCode 0689 - Maximum Sum of 3 Non-Overlapping Subarrays
// https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/

public class Solution {
    public int[] MaxSumOfThreeSubarrays(int[] nums, int k) {
        int n = nums.Length, windows = n - k + 1;
        int[] sums = new int[windows];
        int total = 0;
        for (int i = 0; i < k; i++) total += nums[i];
        sums[0] = total;
        for (int i = 1; i < windows; i++) {
            total += nums[i + k - 1] - nums[i - 1];
            sums[i] = total;
        }
        int[] left = new int[windows];
        int best = 0;
        for (int i = 0; i < windows; i++) {
            if (sums[i] > sums[best]) best = i;
            left[i] = best;
        }
        int[] right = new int[windows];
        best = windows - 1;
        for (int i = windows - 1; i >= 0; i--) {
            if (sums[i] >= sums[best]) best = i;
            right[i] = best;
        }
        int[] answer = { 0, 0, 0 };
        int bestTotal = -1;
        for (int mid = k; mid < windows - k; mid++) {
            int l = left[mid - k], r = right[mid + k];
            int cur = sums[l] + sums[mid] + sums[r];
            if (cur > bestTotal) {
                bestTotal = cur;
                answer = new[] { l, mid, r };
            }
        }
        return answer;
    }
}
