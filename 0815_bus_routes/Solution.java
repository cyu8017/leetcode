// LeetCode 0815 - Bus Routes
// https://leetcode.com/problems/bus-routes/

import java.util.*;

class Solution {
    public int numBusesToDestination(int[][] routes, int source, int target) {
        if (source == target) return 0;
        Map<Integer, List<Integer>> stopToBuses = new HashMap<>();
        for (int bus = 0; bus < routes.length; bus++) {
            for (int stop : routes[bus]) {
                stopToBuses.computeIfAbsent(stop, k -> new ArrayList<>()).add(bus);
            }
        }
        Queue<int[]> queue = new ArrayDeque<>();
        queue.offer(new int[] {source, 0});
        Set<Integer> seenStops = new HashSet<>();
        seenStops.add(source);
        Set<Integer> seenBuses = new HashSet<>();
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int stop = cur[0], busesTaken = cur[1];
            for (int bus : stopToBuses.getOrDefault(stop, Collections.emptyList())) {
                if (!seenBuses.add(bus)) continue;
                for (int nxt : routes[bus]) {
                    if (nxt == target) return busesTaken + 1;
                    if (seenStops.add(nxt)) queue.offer(new int[] {nxt, busesTaken + 1});
                }
            }
        }
        return -1;
    }
}
