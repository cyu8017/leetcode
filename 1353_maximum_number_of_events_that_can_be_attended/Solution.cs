// LeetCode 1353 - Maximum Number Of Events That Can Be Attended
// https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/

using System.Collections.Generic;
public class Solution {
    public int MaxEvents(int[][] events) {
        System.Array.Sort(events, (a, b) => a[0].CompareTo(b[0]));
        var h = new PriorityQueue<int, int>();
        int i = 0, ans = 0, day = 0, n = events.Length;
        while (i < n || h.Count > 0) {
            if (h.Count == 0) day = System.Math.Max(day, events[i][0]);
            while (i < n && events[i][0] <= day) { h.Enqueue(events[i][1], events[i][1]); i++; }
            while (h.Count > 0 && h.Peek() < day) h.Dequeue();
            if (h.Count > 0) { h.Dequeue(); ans++; day++; }
        }
        return ans;
    }
}
