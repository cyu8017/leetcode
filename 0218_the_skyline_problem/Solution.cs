// LeetCode 0218 - The Skyline Problem
// https://leetcode.com/problems/the-skyline-problem/

using System.Collections.Generic;

public class Solution {
    public IList<IList<int>> GetSkyline(int[][] buildings) {
        var events = new List<(int x, int negH, int end)>();
        foreach (int[] building in buildings) {
            events.Add((building[0], -building[2], building[1]));
            events.Add((building[1], 0, 0));
        }
        events.Sort((a, b) => a.x != b.x ? a.x.CompareTo(b.x) : a.negH.CompareTo(b.negH));

        var result = new List<IList<int>>();
        var live = new PriorityQueue<(int negH, int end), int>();
        live.Enqueue((0, int.MaxValue), 0);

        foreach ((int x, int negH, int end) in events) {
            while (live.Count > 0 && live.Peek().end <= x) {
                live.Dequeue();
            }
            if (negH != 0) {
                live.Enqueue((negH, end), negH);
            }
            int height = -live.Peek().negH;
            if (result.Count == 0 || result[result.Count - 1][1] != height) {
                result.Add(new List<int> { x, height });
            }
        }
        return result;
    }
}
