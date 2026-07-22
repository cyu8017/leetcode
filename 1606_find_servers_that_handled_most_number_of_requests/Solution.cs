// LeetCode 1606 - Find Servers That Handled Most Number of Requests
// https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public IList<int> BusiestServers(int k, int[] arrival, int[] load) {
        var free = new SortedSet<int>(Enumerable.Range(0, k));
        var busy = new PriorityQueue<int, int>();
        var count = new int[k];
        for (int i = 0; i < arrival.Length; i++) {
            int t = arrival[i];
            while (busy.Count > 0 && busy.TryPeek(out int server, out int end) && end <= t) {
                busy.Dequeue();
                free.Add(server);
            }
            if (free.Count == 0) continue;
            int start = i % k;
            var view = free.GetViewBetween(start, int.MaxValue);
            int chosen = view.Count > 0 ? view.Min : free.Min;
            free.Remove(chosen);
            count[chosen]++;
            busy.Enqueue(chosen, t + load[i]);
        }
        int best = count.Max();
        var ans = new List<int>();
        for (int i = 0; i < k; i++) if (count[i] == best) ans.Add(i);
        return ans;
    }
}
