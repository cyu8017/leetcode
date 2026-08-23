// LeetCode 2398 - Maximum Number of Robots Within Budget
// https://leetcode.com/problems/maximum-number-of-robots-within-budget/

using System;
using System.Collections.Generic;

public class Solution {
    public int MaximumRobots(int[] chargeTimes, int[] runningCosts, long budget) {
        int n = chargeTimes.Length;
        int left = 0;
        long sum = 0;
        var dq = new LinkedList<int>();
        int ans = 0;
        for (int right = 0; right < n; right++) {
            while (dq.Count > 0 && chargeTimes[dq.Last.Value] <= chargeTimes[right]) dq.RemoveLast();
            dq.AddLast(right);
            sum += runningCosts[right];
            while (left <= right && (long)chargeTimes[dq.First.Value] + (long)(right - left + 1) * sum > budget) {
                if (dq.First.Value == left) dq.RemoveFirst();
                sum -= runningCosts[left];
                left++;
            }
            ans = Math.Max(ans, right - left + 1);
        }
        return ans;
    }
}
