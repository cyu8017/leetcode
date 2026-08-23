// LeetCode 0719 - Find K-th Smallest Pair Distance
// https://leetcode.com/problems/find-k-th-smallest-pair-distance/

using System;

public class Solution {
    public int SmallestDistancePair(int[] nums, int k) {
        Array.Sort(nums);
        int lo = 0, hi = nums[nums.Length - 1] - nums[0];
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (CountPairs(nums, mid) >= k) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }

    private int CountPairs(int[] nums, int distance) {
        int count = 0, left = 0;
        for (int right = 0; right < nums.Length; right++) {
            while (nums[right] - nums[left] > distance) left++;
            count += right - left;
        }
        return count;
    }
}
