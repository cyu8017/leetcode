// LeetCode 2332 - The Latest Time to Catch a Bus
// https://leetcode.com/problems/the-latest-time-to-catch-a-bus/

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

class Solution {
    public int latestTimeCatchTheBus(int[] buses, int[] passengers, int capacity) {
        Arrays.sort(buses);
        Arrays.sort(passengers);
        int pos = 0;
        for (int bi = 0; bi < buses.length; bi++) {
            int bus = buses[bi];
            int cap = capacity;
            while (cap > 0 && pos < passengers.length && passengers[pos] <= bus) {
                pos++;
                cap--;
            }
            if (bi == buses.length - 1) {
                int cand = bus;
                if (cap == 0) cand = passengers[pos - 1];
                Set<Integer> taken = new HashSet<>();
                for (int p : passengers) taken.add(p);
                while (taken.contains(cand)) cand--;
                return cand;
            }
        }
        return -1;
    }
}
