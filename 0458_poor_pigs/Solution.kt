// LeetCode 0458 - Poor Pigs
// https://leetcode.com/problems/poor-pigs/

class Solution {
    fun poorPigs(buckets: Int, minutesToDie: Int, minutesToTest: Int): Int {
        val states = minutesToTest / minutesToDie + 1
        var pigs = 0
        var capacity = 1
        while (capacity < buckets) {
            pigs++
            capacity *= states
        }
        return pigs
    }
}
