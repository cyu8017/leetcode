// LeetCode 0632 - Smallest Range Covering Elements from K Lists
// https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

import java.util.List;
import java.util.PriorityQueue;

class Solution {
    public int[] smallestRange(List<List<Integer>> nums) {
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        int currentMax = Integer.MIN_VALUE;
        for (int i = 0; i < nums.size(); ++i) {
            int val = nums.get(i).get(0);
            heap.offer(new int[] {val, i, 0});
            currentMax = Math.max(currentMax, val);
        }
        int bestLeft = heap.peek()[0];
        int bestRight = currentMax;
        while (true) {
            int[] top = heap.poll();
            int value = top[0];
            int listIndex = top[1];
            int index = top[2];
            if (currentMax - value < bestRight - bestLeft) {
                bestLeft = value;
                bestRight = currentMax;
            }
            if (index + 1 == nums.get(listIndex).size()) {
                break;
            }
            int nxt = nums.get(listIndex).get(index + 1);
            heap.offer(new int[] {nxt, listIndex, index + 1});
            currentMax = Math.max(currentMax, nxt);
        }
        return new int[] {bestLeft, bestRight};
    }
}
