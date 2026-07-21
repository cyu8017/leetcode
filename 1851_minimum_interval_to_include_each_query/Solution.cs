// LeetCode 1851 - Minimum Interval to Include Each Query
// https://leetcode.com/problems/minimum-interval-to-include-each-query/

public class Solution {
    public int[] MinInterval(int[][] intervals, int[] queries) {
        Array.Sort(intervals, (a, b) => a[0].CompareTo(b[0]));
        var indexed = new (int idx, int query)[queries.Length];
        for (int i = 0; i < queries.Length; i++) {
            indexed[i] = (i, queries[i]);
        }
        Array.Sort(indexed, (a, b) => a.query.CompareTo(b.query));

        var heap = new PriorityQueue<(int size, int right), int>();
        var answer = new int[queries.Length];
        Array.Fill(answer, -1);
        int intervalIdx = 0;

        foreach (var (queryIdx, query) in indexed) {
            while (intervalIdx < intervals.Length && intervals[intervalIdx][0] <= query) {
                int left = intervals[intervalIdx][0];
                int right = intervals[intervalIdx][1];
                int size = right - left + 1;
                heap.Enqueue((size, right), size);
                intervalIdx++;
            }
            while (heap.Count > 0 && heap.Peek().right < query) {
                heap.Dequeue();
            }
            if (heap.Count > 0) {
                answer[queryIdx] = heap.Peek().size;
            }
        }
        return answer;
    }
}
