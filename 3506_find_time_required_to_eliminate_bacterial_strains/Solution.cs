// LeetCode 3506 - Find Time Required to Eliminate Bacterial Strains
// https://leetcode.com/problems/find-time-required-to-eliminate-bacterial-strains/

using System.Collections.Generic;

public class Solution {
    public long MinEliminationTime(int[] timeReq, int splitTime) {
        var pq = new PriorityQueue<int, int>();
        foreach (int v in timeReq) pq.Enqueue(v, v);
        while (pq.Count > 1) {
            pq.Dequeue();
            int x = pq.Dequeue();
            pq.Enqueue(x + splitTime, x + splitTime);
        }
        return pq.Peek();
    }
}
