// LeetCode 1942 - The Number of the Smallest Unoccupied Chair
// https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int SmallestChair(int[][] times, int targetFriend) {
        var order = Enumerable.Range(0, times.Length).OrderBy(i => times[i][0]).ToArray();
        var free = new PriorityQueue<int, int>();
        int nextChair = 0;
        var leaving = new PriorityQueue<(int leave, int chair), int>();
        foreach (int i in order) {
            int arr = times[i][0], leave = times[i][1];
            while (leaving.Count > 0 && leaving.Peek().leave <= arr) {
                var (_, chair) = leaving.Dequeue();
                free.Enqueue(chair, chair);
            }
            int ch;
            if (free.Count > 0) ch = free.Dequeue();
            else ch = nextChair++;
            if (i == targetFriend) return ch;
            leaving.Enqueue((leave, ch), leave);
        }
        return -1;
    }
}