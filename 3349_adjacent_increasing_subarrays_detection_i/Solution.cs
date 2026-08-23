// LeetCode 3349 - Adjacent Increasing Subarrays Detection I
// https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/

using System.Collections.Generic;

public class Solution {
    public bool HasIncreasingSubarrays(IList<int> nums, int k) {
        int n = nums.Count;
        bool Inc(int start) {
            for (int i = start; i + 1 < start + k; i++) {
                if (nums[i] >= nums[i + 1]) return false;
            }
            return true;
        }
        for (int i = 0; i + 2 * k <= n; i++) {
            if (Inc(i) && Inc(i + k)) return true;
        }
        return false;
    }
}
