// LeetCode 1199 - Minimum Time to Build Blocks
// https://leetcode.com/problems/minimum-time-to-build-blocks/

using System.Collections.Generic;

public class Solution {
    public int MinBuildTime(int[] blocks, int split) {
        var heap = new PriorityQueue<int, int>();
        foreach (int b in blocks) heap.Enqueue(b, b);
        while (heap.Count > 1) {
            heap.Dequeue();
            int top = heap.Dequeue();
            heap.Enqueue(top + split, top + split);
        }
        return heap.Peek();
    }
}
