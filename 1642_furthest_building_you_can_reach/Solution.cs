// LeetCode 1642 - Furthest Building You Can Reach
// https://leetcode.com/problems/furthest-building-you-can-reach/

using System.Collections.Generic;

public class Solution {
    public int FurthestBuilding(int[] heights, int bricks, int ladders) {
        var climbs = new PriorityQueue<int, int>();
        for (int i = 0; i + 1 < heights.Length; i++) {
            int d = heights[i + 1] - heights[i];
            if (d <= 0) continue;
            climbs.Enqueue(d, d);
            if (climbs.Count > ladders) bricks -= climbs.Dequeue();
            if (bricks < 0) return i;
        }
        return heights.Length - 1;
    }
}
