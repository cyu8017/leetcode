// LeetCode 2410 - Maximum Matching of Players With Trainers
// https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

class Solution {
    fun matchPlayersAndTrainers(players: IntArray, trainers: IntArray): Int {
        players.sort()
        trainers.sort()
        var i = 0
        var j = 0
        var ans = 0
        while (i < players.size && j < trainers.size) {
            if (players[i] <= trainers[j]) {
                ans++
                i++
                j++
            } else j++
        }
        return ans
    }
}
