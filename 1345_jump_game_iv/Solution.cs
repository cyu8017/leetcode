// LeetCode 1345 - Jump Game Iv
// https://leetcode.com/problems/jump-game-iv/

using System.Collections.Generic;
public class Solution {
    public int MinJumps(int[] arr) {
        var positions = new Dictionary<int, List<int>>();
        for (int i = 0; i < arr.Length; i++) {
            if (!positions.ContainsKey(arr[i])) positions[arr[i]] = new List<int>();
            positions[arr[i]].Add(i);
        }
        var queue = new Queue<int>();
        var seen = new HashSet<int> { 0 };
        queue.Enqueue(0);
        int steps = 0;
        while (queue.Count > 0) {
            int size = queue.Count;
            for (int s = 0; s < size; s++) {
                int i = queue.Dequeue();
                if (i == arr.Length - 1) return steps;
                var nexts = new List<int>();
                if (positions.ContainsKey(arr[i])) { nexts.AddRange(positions[arr[i]]); positions.Remove(arr[i]); }
                nexts.Add(i - 1); nexts.Add(i + 1);
                foreach (int j in nexts) {
                    if (j >= 0 && j < arr.Length && seen.Add(j)) queue.Enqueue(j);
                }
            }
            steps++;
        }
        return -1;
    }
}
