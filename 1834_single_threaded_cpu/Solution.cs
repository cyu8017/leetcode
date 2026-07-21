// LeetCode 1834 - Single-Threaded CPU
// https://leetcode.com/problems/single-threaded-cpu/

using System;
using System.Collections.Generic;

public class Solution {
    public int[] GetOrder(int[][] tasks) {
        int n = tasks.Length;
        var indexed = new (int idx, int enqueue, int proc)[n];
        for (int i = 0; i < n; i++) {
            indexed[i] = (i, tasks[i][0], tasks[i][1]);
        }
        Array.Sort(indexed, (a, b) => {
            int cmp = a.enqueue.CompareTo(b.enqueue);
            return cmp != 0 ? cmp : a.idx.CompareTo(b.idx);
        });

        var heap = new PriorityQueue<int, (int proc, int idx)>();
        var order = new List<int>();
        long time = 0;
        int iPtr = 0;

        while (iPtr < n || heap.Count > 0) {
            if (iPtr < n && heap.Count == 0) {
                time = Math.Max(time, indexed[iPtr].enqueue);
            }
            while (iPtr < n && indexed[iPtr].enqueue <= time) {
                heap.Enqueue(indexed[iPtr].idx, (indexed[iPtr].proc, indexed[iPtr].idx));
                iPtr++;
            }
            heap.TryDequeue(out int idx, out var priority);
            time += priority.proc;
            order.Add(idx);
        }
        return order.ToArray();
    }
}
