// LeetCode 1942 - The Number of the Smallest Unoccupied Chair
// https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/

import java.util.*;

class Solution {
    public int smallestChair(int[][] times, int targetFriend) {
        Integer[] order = new Integer[times.length];
        for (int i = 0; i < times.length; i++) order[i] = i;
        Arrays.sort(order, Comparator.comparingInt(i -> times[i][0]));
        PriorityQueue<Integer> free = new PriorityQueue<>();
        PriorityQueue<int[]> leaving = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        int nextChair = 0;
        for (int i : order) {
            int arr = times[i][0], leave = times[i][1];
            while (!leaving.isEmpty() && leaving.peek()[0] <= arr) free.offer(leaving.poll()[1]);
            int chair = free.isEmpty() ? nextChair++ : free.poll();
            if (i == targetFriend) return chair;
            leaving.offer(new int[]{leave, chair});
        }
        return -1;
    }
}
