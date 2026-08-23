// LeetCode 2059 - Minimum Operations to Convert Number
// https://leetcode.com/problems/minimum-operations-to-convert-number/

using System.Collections.Generic;

public class Solution {
    public int MinimumOperations(int[] nums, int start, int goal) {
        if (start == goal) return 0;
        var vis = new HashSet<int> { start };
        var q = new Queue<int>();
        q.Enqueue(start);
        int steps = 0;
        while (q.Count > 0) {
            steps++;
            int sz = q.Count;
            while (sz-- > 0) {
                int cur = q.Dequeue();
                foreach (int x in nums) {
                    foreach (int nxt in new[] { cur + x, cur - x, cur ^ x }) {
                        if (nxt == goal) return steps;
                        if (nxt >= 0 && nxt <= 1000 && vis.Add(nxt)) q.Enqueue(nxt);
                    }
                }
            }
        }
        return -1;
    }
}
