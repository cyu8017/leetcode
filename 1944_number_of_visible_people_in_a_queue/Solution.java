// LeetCode 1944 - Number of Visible People in a Queue
// https://leetcode.com/problems/number-of-visible-people-in-a-queue/

import java.util.*;

class Solution {
    public int[] canSeePersonsCount(int[] heights) {
        int n = heights.length;
        int[] ans = new int[n];
        Deque<Integer> stack = new ArrayDeque<>();
        for (int i = n - 1; i >= 0; i--) {
            int count = 0;
            while (!stack.isEmpty() && heights[i] > stack.peek()) {
                stack.pop();
                count++;
            }
            if (!stack.isEmpty()) count++;
            ans[i] = count;
            stack.push(heights[i]);
        }
        return ans;
    }
}
