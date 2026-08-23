// LeetCode 2208 - Minimum Operations to Halve Array Sum
// https://leetcode.com/problems/minimum-operations-to-halve-array-sum/

using System.Collections.Generic;

public class Solution {
    public int HalveArray(int[] nums) {
        var h = new PriorityQueue<double, double>();
        double sum = 0;
        foreach (int x in nums) {
            h.Enqueue(x, -x);
            sum += x;
        }
        double target = sum / 2;
        int ans = 0;
        while (sum > target) {
            h.TryDequeue(out double top, out _);
            double x = top / 2;
            sum -= x;
            h.Enqueue(x, -x);
            ans++;
        }
        return ans;
    }
}
