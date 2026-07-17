// LeetCode 1793 - Maximum Score of a Good Subarray
// https://leetcode.com/problems/maximum-score-of-a-good-subarray/

import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public int maximumScore(int[] nums, int k) {
        int n = nums.length;
        Deque<Integer> stack = new ArrayDeque<>();
        long ans = 0;
        for (int i = 0; i <= n; i++) {
            while (!stack.isEmpty() && (i == n || nums[i] < nums[stack.peek()])) {
                int mid = stack.pop();
                int left = stack.isEmpty() ? 0 : stack.peek() + 1;
                int right = i - 1;
                if (left <= k && k <= right) {
                    ans = Math.max(ans, (long) nums[mid] * (right - left + 1));
                }
            }
            stack.push(i);
        }
        return (int) ans;
    }
}
