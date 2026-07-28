// LeetCode 1046 - Last Stone Weight
// https://leetcode.com/problems/last-stone-weight/

using System.Collections.Generic;

public class Solution {
    public int LastStoneWeight(int[] stones) {
        var pq = new PriorityQueue<int, int>();
        foreach (int s in stones) pq.Enqueue(s, -s);
        while (pq.Count > 1) {
            int a = pq.Dequeue(), b = pq.Dequeue();
            if (a != b) pq.Enqueue(a - b, -(a - b));
        }
        return pq.Count == 0 ? 0 : pq.Dequeue();
    }
}
