// LeetCode 1439 - Find The Kth Smallest Sum Of A Matrix With Sorted Rows
// https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/

import java.util.*;

class Solution {
    public int kthSmallest(int[][] mat, int k) {
        List<Integer> sums = new ArrayList<>();
        sums.add(0);
        for (int[] row : mat) {
            PriorityQueue<int[]> heap = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
            heap.offer(new int[]{sums.get(0) + row[0], 0, 0});
            List<Integer> merged = new ArrayList<>();
            while (!heap.isEmpty() && merged.size() < k) {
                int[] cur = heap.poll();
                int value = cur[0], i = cur[1], j = cur[2];
                merged.add(value);
                if (j + 1 < row.length) heap.offer(new int[]{sums.get(i) + row[j + 1], i, j + 1});
                if (j == 0 && i + 1 < sums.size()) heap.offer(new int[]{sums.get(i + 1) + row[0], i + 1, 0});
            }
            sums = merged;
        }
        return sums.get(k - 1);
    }
}
