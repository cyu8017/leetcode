// LeetCode 1776 - Car Fleet II
// https://leetcode.com/problems/car-fleet-ii/

import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public double[] getCollisionTimes(int[][] cars) {
        int n = cars.length;
        double[] ans = new double[n];
        java.util.Arrays.fill(ans, -1.0);
        Deque<Integer> stack = new ArrayDeque<>();
        for (int i = n - 1; i >= 0; i--) {
            int pos = cars[i][0];
            int speed = cars[i][1];
            while (!stack.isEmpty()) {
                int j = stack.peek();
                if (speed <= cars[j][1]) {
                    stack.pop();
                    continue;
                }
                double t = (double) (cars[j][0] - pos) / (speed - cars[j][1]);
                if (ans[j] < 0 || t <= ans[j]) {
                    ans[i] = t;
                    break;
                }
                stack.pop();
            }
            stack.push(i);
        }
        return ans;
    }
}
