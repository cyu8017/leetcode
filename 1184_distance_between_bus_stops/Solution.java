// LeetCode 1184 - Distance Between Bus Stops
// https://leetcode.com/problems/distance-between-bus-stops/

class Solution {
    public int distanceBetweenBusStops(int[] distance, int start, int destination) {
        if (start > destination) { int t = start; start = destination; destination = t; }
        int clockwise = 0, total = 0;
        for (int i = 0; i < distance.length; i++) {
            total += distance[i];
            if (i >= start && i < destination) clockwise += distance[i];
        }
        return Math.min(clockwise, total - clockwise);
    }
}
