// LeetCode 1334 - Find the City With the Smallest Number of Neighbors at a Threshold Distance
// https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

class Solution {
    fun findTheCity(n: Int, edges: Array<IntArray>, distanceThreshold: Int): Int {
        val inf = 1_000_000_000_000_000L
        val dist = Array(n) { LongArray(n) { inf } }
        for (i in 0 until n) dist[i][i] = 0
        for (e in edges) {
            dist[e[0]][e[1]] = e[2].toLong()
            dist[e[1]][e[0]] = e[2].toLong()
        }
        for (k in 0 until n) {
            for (i in 0 until n) {
                for (j in 0 until n) {
                    dist[i][j] = minOf(dist[i][j], dist[i][k] + dist[k][j])
                }
            }
        }
        var bestCity = 0
        var bestCount = Int.MAX_VALUE
        for (city in 0 until n) {
            val count = dist[city].count { it <= distanceThreshold }
            if (count < bestCount || (count == bestCount && city > bestCity)) {
                bestCount = count
                bestCity = city
            }
        }
        return bestCity
    }
}
