// LeetCode 1962 - Remove Stones to Minimize the Total
// https://leetcode.com/problems/remove-stones-to-minimize-the-total/

import java.util.*;

class Solution {
    public int minStoneSum(int[] piles, int k) {
        PriorityQueue<Integer> heap = new PriorityQueue<>(Collections.reverseOrder());
        for (int p : piles) heap.offer(p);
        for (int i = 0; i < k; i++) {
            int x = heap.poll();
            heap.offer(x - x / 2);
        }
        int sum = 0;
        while (!heap.isEmpty()) sum += heap.poll();
        return sum;
    }
}
