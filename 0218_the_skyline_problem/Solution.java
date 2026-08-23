// LeetCode 0218 - The Skyline Problem
// https://leetcode.com/problems/the-skyline-problem/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;

class Solution {
    public List<List<Integer>> getSkyline(int[][] buildings) {
        List<int[]> events = new ArrayList<>();
        for (int[] building : buildings) {
            events.add(new int[] { building[0], -building[2], building[1] });
            events.add(new int[] { building[1], 0, 0 });
        }
        events.sort(Comparator.comparingInt((int[] event) -> event[0])
            .thenComparingInt(event -> event[1]));

        List<List<Integer>> result = new ArrayList<>();
        PriorityQueue<int[]> live = new PriorityQueue<>(
            Comparator.comparingInt((int[] item) -> item[0])
        );
        live.offer(new int[] { 0, Integer.MAX_VALUE });

        for (int[] event : events) {
            int x = event[0];
            int negH = event[1];
            int end = event[2];
            while (live.peek()[1] <= x) {
                live.poll();
            }
            if (negH != 0) {
                live.offer(new int[] { negH, end });
            }
            int height = -live.peek()[0];
            if (result.isEmpty() || result.get(result.size() - 1).get(1) != height) {
                result.add(Arrays.asList(x, height));
            }
        }
        return result;
    }
}
