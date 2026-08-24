// LeetCode 2332 - The Latest Time to Catch a Bus
// https://leetcode.com/problems/the-latest-time-to-catch-a-bus/

class Solution {
    fun latestTimeCatchTheBus(buses: IntArray, passengers: IntArray, capacity: Int): Int {
        buses.sort()
        passengers.sort()
        var pos = 0
        for (bi in buses.indices) {
            val bus = buses[bi]
            var cap = capacity
            while (cap > 0 && pos < passengers.size && passengers[pos] <= bus) {
                pos++
                cap--
            }
            if (bi == buses.lastIndex) {
                var cand = if (cap == 0) passengers[pos - 1] else bus
                val taken = passengers.toHashSet()
                while (cand in taken) cand--
                return cand
            }
        }
        return -1
    }
}
