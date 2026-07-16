// LeetCode 0544 - Output Contest Matches
// https://leetcode.com/problems/output-contest-matches/

class Solution {
    fun findContestMatch(n: Int): String {
        var teams = (1..n).map { it.toString() }.toMutableList()
        while (teams.size > 1) {
            val nextRound = mutableListOf<String>()
            for (i in 0 until teams.size / 2) {
                nextRound.add("(${teams[i]},${teams[teams.size - 1 - i]})")
            }
            teams = nextRound
        }
        return teams[0]
    }
}
