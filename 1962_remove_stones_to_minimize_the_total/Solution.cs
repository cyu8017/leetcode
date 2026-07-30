// LeetCode 1962 - Remove Stones to Minimize the Total
// https://leetcode.com/problems/remove-stones-to-minimize-the-total/

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int MinStoneSum(int[] piles, int k) {
        var pq = new PriorityQueue<int, int>();
        foreach (int p in piles) pq.Enqueue(p, -p);
        for (int i = 0; i < k; i++) {
            int x = pq.Dequeue();
            int nx = x - x / 2;
            pq.Enqueue(nx, -nx);
        }
        int sum = 0;
        while (pq.Count > 0) sum += pq.Dequeue();
        return sum;
    }
}