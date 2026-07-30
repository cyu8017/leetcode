// LeetCode 1167 - Minimum Cost to Connect Sticks
// https://leetcode.com/problems/minimum-cost-to-connect-sticks/

using System.Collections.Generic;

public class Solution {
    public int ConnectSticks(int[] sticks) {
        if (sticks.Length <= 1) return 0;
        var pq = new PriorityQueue<int, int>();
        foreach (int s in sticks) pq.Enqueue(s, s);
        int ans = 0;
        while (pq.Count > 1) {
            int cost = pq.Dequeue() + pq.Dequeue();
            ans += cost;
            pq.Enqueue(cost, cost);
        }
        return ans;
    }
}
