// LeetCode 1642 - Furthest Building You Can Reach
// https://leetcode.com/problems/furthest-building-you-can-reach/

import java.util.*;

class Solution {
    public int furthestBuilding(int[] heights, int bricks, int ladders) {
        PriorityQueue<Integer> climbs = new PriorityQueue<>();
        for (int i = 0; i < heights.length - 1; i++) {
            int d = heights[i + 1] - heights[i];
            if (d <= 0) continue;
            climbs.offer(d);
            if (climbs.size() > ladders) bricks -= climbs.poll();
            if (bricks < 0) return i;
        }
        return heights.length - 1;
    }
}
