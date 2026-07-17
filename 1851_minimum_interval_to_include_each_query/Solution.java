// LeetCode 1851 - Minimum Interval to Include Each Query
// https://leetcode.com/problems/minimum-interval-to-include-each-query/

import java.util.Arrays;
import java.util.PriorityQueue;

class Solution {
    public int[] minInterval(int[][] intervals, int[] queries) {
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        int[][] indexedQueries = new int[queries.length][2];
        for (int i = 0; i < queries.length; i++) {
            indexedQueries[i][0] = i;
            indexedQueries[i][1] = queries[i];
        }
        Arrays.sort(indexedQueries, (a, b) -> Integer.compare(a[1], b[1]));

        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        int[] answer = new int[queries.length];
        Arrays.fill(answer, -1);
        int intervalIdx = 0;

        for (int[] item : indexedQueries) {
            int queryIdx = item[0];
            int query = item[1];

            while (intervalIdx < intervals.length && intervals[intervalIdx][0] <= query) {
                int left = intervals[intervalIdx][0];
                int right = intervals[intervalIdx][1];
                heap.offer(new int[] { right - left + 1, right });
                intervalIdx++;
            }

            while (!heap.isEmpty() && heap.peek()[1] < query) {
                heap.poll();
            }

            if (!heap.isEmpty()) {
                answer[queryIdx] = heap.peek()[0];
            }
        }

        return answer;
    }
}
