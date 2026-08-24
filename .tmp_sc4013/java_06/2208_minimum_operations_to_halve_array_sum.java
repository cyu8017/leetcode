// LeetCode 2208 - Minimum Operations to Halve Array Sum
// https://leetcode.com/problems/minimum-operations-to-halve-array-sum/

import java.util.PriorityQueue;

class Solution {
    public int halveArray(int[] nums) {
        PriorityQueue<Double> h = new PriorityQueue<>((a, b) -> Double.compare(b, a));
        double sum = 0;
        for (int x : nums) {
            h.offer((double) x);
            sum += x;
        }
        double target = sum / 2;
        int ans = 0;
        while (sum > target) {
            double top = h.poll();
            double x = top / 2;
            sum -= x;
            h.offer(x);
            ans++;
        }
        return ans;
    }
}
