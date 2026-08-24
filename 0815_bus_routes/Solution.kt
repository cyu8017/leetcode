// LeetCode 0815 - Bus Routes
// https://leetcode.com/problems/bus-routes/

class Solution {
    fun numBusesToDestination(routes: Array<IntArray>, source: Int, target: Int): Int {
        if (source == target) return 0
        var stopToBuses = HashMap<Int, MutableList<Int>>()
        for (bus in 0 until routes.size) {
            for (stop in routes[bus]) {
                stopToBuses.computeIfAbsent(stop, k -> ArrayList()).add(bus)
            }
        }
        var queue = ArrayDeque<IntArray>()
        queue.offer(intArrayOf(source, 0))
        var seenStops = HashSet<Int>()
        seenStops.add(source)
        var seenBuses = HashSet<Int>()
        while (!queue.isEmpty()) {
            var cur = queue.poll()
            var stop = cur[0]
            var busesTaken = cur[1]
            for (bus in stopToBuses.getOrDefault(stop, Collections.emptyList())) {
                if (!seenBuses.add(bus)) continue
                for (nxt in routes[bus]) {
                    if (nxt == target) return busesTaken + 1
                    if (seenStops.add(nxt)) queue.offer(intArrayOf(nxt, busesTaken + 1))
                }
            }
        }
        return -1
    }
}
