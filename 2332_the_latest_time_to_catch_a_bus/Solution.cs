// LeetCode 2332 - The Latest Time to Catch a Bus
// https://leetcode.com/problems/the-latest-time-to-catch-a-bus/

using System;
using System.Collections.Generic;

public class Solution {
    public int LatestTimeCatchTheBus(int[] buses, int[] passengers, int capacity) {
        Array.Sort(buses);
        Array.Sort(passengers);
        int pos = 0;
        for (int bi = 0; bi < buses.Length; bi++) {
            int bus = buses[bi];
            int cap = capacity;
            while (cap > 0 && pos < passengers.Length && passengers[pos] <= bus) {
                pos++;
                cap--;
            }
            if (bi == buses.Length - 1) {
                int cand = bus;
                if (cap == 0) cand = passengers[pos - 1];
                var taken = new HashSet<int>(passengers);
                while (taken.Contains(cand)) cand--;
                return cand;
            }
        }
        return -1;
    }
}
