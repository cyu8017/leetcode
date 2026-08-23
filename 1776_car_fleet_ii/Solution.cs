// LeetCode 1776 - Car Fleet II
// https://leetcode.com/problems/car-fleet-ii/

using System.Collections.Generic;

public class Solution {
    public double[] GetCollisionTimes(int[][] cars) {
        int n = cars.Length;
        double[] ans = new double[n];
        for (int i = 0; i < n; i++) {
            ans[i] = -1.0;
        }
        var stack = new Stack<int>();
        for (int i = n - 1; i >= 0; i--) {
            int pos = cars[i][0];
            int speed = cars[i][1];
            while (stack.Count > 0) {
                int j = stack.Peek();
                if (speed <= cars[j][1]) {
                    stack.Pop();
                    continue;
                }
                double t = (double)(cars[j][0] - pos) / (speed - cars[j][1]);
                if (ans[j] < 0 || t <= ans[j]) {
                    ans[i] = t;
                    break;
                }
                stack.Pop();
            }
            stack.Push(i);
        }
        return ans;
    }
}
