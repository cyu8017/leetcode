// LeetCode 1847 - Closest Room
// https://leetcode.com/problems/closest-room/

import java.util.TreeSet

class Solution {
    fun closestRoom(rooms: Array<IntArray>, queries: Array<IntArray>): IntArray {
        rooms.sortBy { it[1] }
        val indexedQueries = queries.indices.sortedByDescending { queries[it][1] }
        val availableIds = TreeSet<Int>()
        var roomIndex = rooms.size - 1
        val answer = IntArray(queries.size) { -1 }

        for (queryIndex in indexedQueries) {
            val preferred = queries[queryIndex][0]
            val minSize = queries[queryIndex][1]
            while (roomIndex >= 0 && rooms[roomIndex][1] >= minSize) {
                availableIds.add(rooms[roomIndex][0])
                roomIndex--
            }
            if (availableIds.isEmpty()) continue

            var bestId = -1
            var bestDist = Int.MAX_VALUE
            val ceil = availableIds.ceiling(preferred)
            val floor = availableIds.floor(preferred)
            if (ceil != null) {
                val dist = kotlin.math.abs(ceil - preferred)
                if (dist < bestDist || (dist == bestDist && ceil < bestId)) {
                    bestId = ceil
                    bestDist = dist
                }
            }
            if (floor != null) {
                val dist = kotlin.math.abs(floor - preferred)
                if (dist < bestDist || (dist == bestDist && floor < bestId)) {
                    bestId = floor
                }
            }
            answer[queryIndex] = bestId
        }
        return answer
    }
}
