// LeetCode 0719 - Find K-th Smallest Pair Distance
// https://leetcode.com/problems/find-k-th-smallest-pair-distance/

import java.util.*;

class Solution {
    public int smallestDistancePair(int[] nums, int k) {
        Arrays.sort(nums);
        int lo = 0, hi = nums[nums.length - 1] - nums[0];
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (countPairs(nums, mid) >= k) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }

    private int countPairs(int[] nums, int distance) {
        int count = 0, left = 0;
        for (int right = 0; right < nums.length; right++) {
            while (nums[right] - nums[left] > distance) left++;
            count += right - left;
        }
        return count;
    }
}
