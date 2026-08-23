// LeetCode 0773 - Sliding Puzzle
// https://leetcode.com/problems/sliding-puzzle/

using System.Collections.Generic;
using System.Text;

public class Solution {
    public int SlidingPuzzle(int[][] board) {
        var start = new StringBuilder();
        foreach (var row in board) foreach (int cell in row) start.Append(cell);
        const string target = "123450";
        var neighbors = new Dictionary<int, int[]> {
            {0, new[]{1,3}}, {1, new[]{0,2,4}}, {2, new[]{1,5}},
            {3, new[]{0,4}}, {4, new[]{1,3,5}}, {5, new[]{2,4}},
        };
        var q = new Queue<(string, int)>();
        var seen = new HashSet<string> { start.ToString() };
        q.Enqueue((start.ToString(), 0));
        while (q.Count > 0) {
            var (state, steps) = q.Dequeue();
            if (state == target) return steps;
            int zero = state.IndexOf('0');
            foreach (int nei in neighbors[zero]) {
                char[] nxt = state.ToCharArray();
                (nxt[zero], nxt[nei]) = (nxt[nei], nxt[zero]);
                string ns = new string(nxt);
                if (seen.Add(ns)) q.Enqueue((ns, steps + 1));
            }
        }
        return -1;
    }
}
