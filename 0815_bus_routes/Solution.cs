// LeetCode 0815 - Bus Routes
// https://leetcode.com/problems/bus-routes/

using System.Collections.Generic;

public class Solution {
    public int NumBusesToDestination(int[][] routes, int source, int target) {
        if (source == target) return 0;
        var stopToBuses = new Dictionary<int, List<int>>();
        for (int bus = 0; bus < routes.Length; bus++) {
            foreach (int stop in routes[bus]) {
                if (!stopToBuses.ContainsKey(stop)) stopToBuses[stop] = new List<int>();
                stopToBuses[stop].Add(bus);
            }
        }
        var queue = new Queue<(int stop, int busesTaken)>();
        queue.Enqueue((source, 0));
        var seenStops = new HashSet<int> { source };
        var seenBuses = new HashSet<int>();
        while (queue.Count > 0) {
            var (stop, busesTaken) = queue.Dequeue();
            if (!stopToBuses.ContainsKey(stop)) continue;
            foreach (int bus in stopToBuses[stop]) {
                if (!seenBuses.Add(bus)) continue;
                foreach (int nxt in routes[bus]) {
                    if (nxt == target) return busesTaken + 1;
                    if (seenStops.Add(nxt)) queue.Enqueue((nxt, busesTaken + 1));
                }
            }
        }
        return -1;
    }
}
