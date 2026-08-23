// LeetCode 0853 - Car Fleet
// https://leetcode.com/problems/car-fleet/

using System;

public class Solution {
    public int CarFleet(int target, int[] position, int[] speed) {
        int n = position.Length;
        var cars = new (int pos, int spd)[n];
        for (int i = 0; i < n; i++) cars[i] = (position[i], speed[i]);
        Array.Sort(cars, (a, b) => b.pos.CompareTo(a.pos));
        int fleets = 0;
        double maxTime = 0.0;
        foreach (var (pos, spd) in cars) {
            double time = (double)(target - pos) / spd;
            if (time > maxTime) { fleets++; maxTime = time; }
        }
        return fleets;
    }
}
