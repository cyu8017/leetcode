// LeetCode 1199 - Minimum Time to Build Blocks
// https://leetcode.com/problems/minimum-time-to-build-blocks/

import java.util.*;

class Solution {
    public int minBuildTime(int[] blocks, int split) {
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        for (int b : blocks) heap.offer(b);
        while (heap.size() > 1) {
            heap.poll();
            heap.offer(heap.poll() + split);
        }
        return heap.peek();
    }
}
