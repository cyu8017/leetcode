// LeetCode 1184 - Distance Between Bus Stops
// https://leetcode.com/problems/distance-between-bus-stops/

using System;
using System.Linq;

public class Solution {
    public int DistanceBetweenBusStops(int[] distance, int start, int destination) {
        if (start > destination) (start, destination) = (destination, start);
        int clockwise = 0;
        for (int i = start; i < destination; i++) clockwise += distance[i];
        return Math.Min(clockwise, distance.Sum() - clockwise);
    }
}
