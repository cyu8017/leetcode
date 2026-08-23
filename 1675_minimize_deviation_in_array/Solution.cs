// LeetCode 1675 - Minimize Deviation in Array
// https://leetcode.com/problems/minimize-deviation-in-array/

using System;
using System.Collections.Generic;

public class Solution {
    public int MinimumDeviation(int[] nums) {
        var pq = new PriorityQueue<int, int>();
        int mn = int.MaxValue;
        foreach (int num in nums) {
            int x = num;
            if ((x & 1) == 1) x *= 2;
            mn = Math.Min(mn, x);
            pq.Enqueue(x, -x);
        }
        int ans = int.MaxValue;
        while (true) {
            int x = pq.Dequeue();
            ans = Math.Min(ans, x - mn);
            if ((x & 1) == 1) return ans;
            x /= 2;
            mn = Math.Min(mn, x);
            pq.Enqueue(x, -x);
        }
    }
}
