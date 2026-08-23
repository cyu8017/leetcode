// LeetCode 0871 - Minimum Number of Refueling Stops
// https://leetcode.com/problems/minimum-number-of-refueling-stops/

import java.util.*;

class Solution {
    public int minRefuelStops(int target, int startFuel, int[][] stations) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        int[][] all = Arrays.copyOf(stations, stations.length + 1);
        all[stations.length] = new int[] {target, 0};
        int ans = 0, prev = 0;
        long fuel = startFuel;
        for (int[] st : all) {
            int pos = st[0], gas = st[1];
            fuel -= pos - prev;
            while (!pq.isEmpty() && fuel < 0) {
                fuel += pq.poll();
                ans++;
            }
            if (fuel < 0) return -1;
            pq.offer(gas);
            prev = pos;
        }
        return ans;
    }
}
