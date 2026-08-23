// LeetCode 0239 - Sliding Window Maximum
// https://leetcode.com/problems/sliding-window-maximum/

import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        Deque<Integer> window = new ArrayDeque<>();
        int[] result = new int[nums.length - k + 1];
        int resultIndex = 0;

        for (int index = 0; index < nums.length; index++) {
            while (!window.isEmpty() && nums[window.peekLast()] <= nums[index]) {
                window.pollLast();
            }
            window.offerLast(index);
            if (window.peekFirst() <= index - k) {
                window.pollFirst();
            }
            if (index >= k - 1) {
                result[resultIndex++] = nums[window.peekFirst()];
            }
        }

        return result;
    }
}
