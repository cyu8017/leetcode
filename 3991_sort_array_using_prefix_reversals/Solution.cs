// LeetCode 3991 - Sort Array Using Prefix Reversals
// https://leetcode.com/problems/sort-array-using-prefix-reversals/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int SortArray(int[] nums, int[] pre) {
        int n = nums.Length;
        string start = string.Join(",", nums);
        string target = string.Join(",", Enumerable.Range(0, n));
        if (start == target) return 0;

        var lengths = pre.Where(i => i >= 2 && i <= n).Distinct().OrderBy(i => i).ToList();
        var visited = new HashSet<string> { start };
        var queue = new Queue<int[]>();
        queue.Enqueue((int[])nums.Clone());
        int steps = 0;

        while (queue.Count > 0) {
            steps++;
            int size = queue.Count;
            for (int t = 0; t < size; t++) {
                int[] cur = queue.Dequeue();
                foreach (int i in lengths) {
                    int[] nxt = (int[])cur.Clone();
                    for (int l = 0, r = i - 1; l < r; l++, r--) {
                        int tmp = nxt[l];
                        nxt[l] = nxt[r];
                        nxt[r] = tmp;
                    }
                    string key = string.Join(",", nxt);
                    if (key == target) return steps;
                    if (visited.Add(key)) queue.Enqueue(nxt);
                }
            }
        }
        return -1;
    }
}
