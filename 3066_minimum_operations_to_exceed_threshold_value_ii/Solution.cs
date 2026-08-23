// LeetCode 3066 - Minimum Operations to Exceed Threshold Value II
// https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

using System.Collections.Generic;

public class Solution {
    public int MinOperations(int[] nums, int k) {
        var pq = new PriorityQueue<long, long>();
        foreach (int x in nums) pq.Enqueue(x, x);
        int ans = 0;
        while (pq.Count > 1 && pq.Peek() < k) {
            long x = pq.Dequeue();
            long y = pq.Dequeue();
            long z = x * 2 + y;
            pq.Enqueue(z, z);
            ans++;
        }
        return ans;
    }
}
