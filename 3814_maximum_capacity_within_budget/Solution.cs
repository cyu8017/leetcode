// LeetCode 3814 - Maximum Capacity Within Budget
// https://leetcode.com/problems/maximum-capacity-within-budget/

using System;
using System.Collections.Generic;

public class Solution {
    public int MaxCapacity(int[] costs, int[] capacity, int budget) {
        var arr = new List<(int cost, int cap)>();
        for (int k = 0; k < costs.Length; k++) {
            if (costs[k] < budget) arr.Add((costs[k], capacity[k]));
        }
        if (arr.Count == 0) return 0;
        arr.Sort((a, b) => a.cost.CompareTo(b.cost));
        int m = arr.Count;
        bool[] alive = new bool[m];
        for (int i = 0; i < m; i++) alive[i] = true;
        var h = new PriorityQueue<(int cap, int idx), (int, int)>();
        for (int i = 0; i < m; i++) h.Enqueue((arr[i].cap, i), (-arr[i].cap, -i));
        while (h.Count > 0 && !alive[h.Peek().idx]) h.Dequeue();
        int ans = h.Peek().cap;
        int ii = 0, j = m - 1;
        while (ii < j) {
            alive[ii] = false;
            while (ii < j && arr[ii].cost + arr[j].cost >= budget) {
                alive[j] = false;
                j--;
            }
            while (h.Count > 0 && !alive[h.Peek().idx]) h.Dequeue();
            if (h.Count > 0) ans = Math.Max(ans, arr[ii].cap + h.Peek().cap);
            ii++;
        }
        return ans;
    }
}
