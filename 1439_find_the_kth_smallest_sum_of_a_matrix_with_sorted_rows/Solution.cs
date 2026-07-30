// LeetCode 1439 - Find The Kth Smallest Sum Of A Matrix With Sorted Rows
// https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/

using System.Collections.Generic;
public class Solution {
    public int KthSmallest(int[][] mat, int k) {
        var sums = new List<int> { 0 };
        foreach (var row in mat) {
            var pq = new PriorityQueue<(int,int,int), int>();
            pq.Enqueue((sums[0] + row[0], 0, 0), sums[0] + row[0]);
            var merged = new List<int>();
            var seen = new HashSet<(int,int)>();
            while (pq.Count > 0 && merged.Count < k) {
                var (value, i, j) = pq.Dequeue();
                if (!seen.Add((i, j))) continue;
                merged.Add(value);
                if (j + 1 < row.Length) pq.Enqueue((sums[i] + row[j + 1], i, j + 1), sums[i] + row[j + 1]);
                if (j == 0 && i + 1 < sums.Count) pq.Enqueue((sums[i + 1] + row[0], i + 1, 0), sums[i + 1] + row[0]);
            }
            sums = merged;
        }
        return sums[k - 1];
    }
}
