// LeetCode 1438 - Longest Continuous Subarray With Absolute Diff Less Than Or Equal To Limit
// https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

import java.util.*;

class Solution {
    public int longestSubarray(int[] nums, int limit) {
        Deque<Integer> maxq = new ArrayDeque<>(), minq = new ArrayDeque<>();
        int left = 0, ans = 0;
        for (int right = 0; right < nums.length; right++) {
            while (!maxq.isEmpty() && nums[maxq.peekLast()] < nums[right]) maxq.pollLast();
            while (!minq.isEmpty() && nums[minq.peekLast()] > nums[right]) minq.pollLast();
            maxq.offerLast(right);
            minq.offerLast(right);
            while (nums[maxq.peekFirst()] - nums[minq.peekFirst()] > limit) {
                if (maxq.peekFirst() == left) maxq.pollFirst();
                if (minq.peekFirst() == left) minq.pollFirst();
                left++;
            }
            ans = Math.max(ans, right - left + 1);
        }
        return ans;
    }
}
