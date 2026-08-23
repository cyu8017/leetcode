// LeetCode 0871 - Minimum Number of Refueling Stops
// https://leetcode.com/problems/minimum-number-of-refueling-stops/

using System.Collections.Generic;

public class Solution {
    public int MinRefuelStops(int target, int startFuel, int[][] stations) {
        var pq = new PriorityQueue<int, int>();
        var list = new List<int[]>(stations) { new int[] { target, 0 } };
        int ans = 0, prev = 0;
        long fuel = startFuel;
        foreach (var st in list) {
            int pos = st[0], gas = st[1];
            fuel -= pos - prev;
            while (pq.Count > 0 && fuel < 0) {
                fuel += pq.Dequeue();
                ans++;
            }
            if (fuel < 0) return -1;
            pq.Enqueue(gas, -gas);
            prev = pos;
        }
        return ans;
    }
}
