// LeetCode 2398 - Maximum Number of Robots Within Budget
// https://leetcode.com/problems/maximum-number-of-robots-within-budget/

import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public int maximumRobots(int[] chargeTimes, int[] runningCosts, long budget) {
        int n = chargeTimes.length;
        int left = 0;
        long sum = 0;
        Deque<Integer> dq = new ArrayDeque<>();
        int ans = 0;
        for (int right = 0; right < n; right++) {
            while (!dq.isEmpty() && chargeTimes[dq.peekLast()] <= chargeTimes[right]) dq.pollLast();
            dq.addLast(right);
            sum += runningCosts[right];
            while (left <= right && (long) chargeTimes[dq.peekFirst()] + (long) (right - left + 1) * sum > budget) {
                if (dq.peekFirst() == left) dq.pollFirst();
                sum -= runningCosts[left];
                left++;
            }
            ans = Math.max(ans, right - left + 1);
        }
        return ans;
    }
}
