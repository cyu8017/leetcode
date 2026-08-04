// LeetCode 1499 - Max Value Of Equation
// https://leetcode.com/problems/max-value-of-equation/

import java.util.*;

class Solution {
    public int findMaxValueOfEquation(int[][] points, int k) {
        Deque<int[]> q = new ArrayDeque<>();
        long ans = Long.MIN_VALUE / 4;
        for (int[] p : points) {
            int x = p[0], y = p[1];
            while (!q.isEmpty() && x - q.peekFirst()[0] > k) q.pollFirst();
            if (!q.isEmpty()) ans = Math.max(ans, (long) x + y + q.peekFirst()[1]);
            int value = y - x;
            while (!q.isEmpty() && q.peekLast()[1] <= value) q.pollLast();
            q.addLast(new int[]{x, value});
        }
        return (int) ans;
    }
}
