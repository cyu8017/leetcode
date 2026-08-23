// LeetCode 3350 - Adjacent Increasing Subarrays Detection II
// https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/

using System.Collections.Generic;

public class Solution {
    public int MaxIncreasingSubarrays(IList<int> nums) {
        int n = nums.Count;
        int[] up = new int[n];
        up[n - 1] = 1;
        for (int i = n - 2; i >= 0; i--) {
            up[i] = (nums[i] < nums[i + 1]) ? up[i + 1] + 1 : 1;
        }
        int lo = 1, hi = n / 2;
        bool Ok(int k) {
            for (int i = 0; i + 2 * k <= n; i++) {
                if (up[i] >= k && up[i + k] >= k) return true;
            }
            return false;
        }
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (Ok(mid)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }
}
