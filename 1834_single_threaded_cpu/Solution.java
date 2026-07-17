// LeetCode 1834 - Single-Threaded CPU
// https://leetcode.com/problems/single-threaded-cpu/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;

class Solution {
    public int[] getOrder(int[][] tasks) {
        int n = tasks.length;
        int[][] indexed = new int[n][3];
        for (int i = 0; i < n; i++) {
            indexed[i][0] = tasks[i][0];
            indexed[i][1] = tasks[i][1];
            indexed[i][2] = i;
        }
        Arrays.sort(indexed, Comparator.comparingInt((int[] task) -> task[0])
                .thenComparingInt(task -> task[2]));

        PriorityQueue<int[]> heap = new PriorityQueue<>(
                Comparator.comparingInt((int[] task) -> task[0])
                        .thenComparingInt(task -> task[1]));
        List<Integer> order = new ArrayList<>();
        int i = 0;
        long time = 0;

        while (i < n || !heap.isEmpty()) {
            if (i < n && heap.isEmpty()) {
                time = Math.max(time, indexed[i][0]);
            }

            while (i < n && indexed[i][0] <= time) {
                heap.offer(new int[] {indexed[i][1], indexed[i][2]});
                i++;
            }

            int[] task = heap.poll();
            time += task[0];
            order.add(task[1]);
        }

        int[] result = new int[order.size()];
        for (int j = 0; j < order.size(); j++) {
            result[j] = order.get(j);
        }
        return result;
    }
}
