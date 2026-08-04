// LeetCode 1125 - Smallest Sufficient Team
// https://leetcode.com/problems/smallest-sufficient-team/

class Solution {
    fun smallestSufficientTeam(req_skills: Array<String>, people: List<List<String>>): IntArray {
        val skillId = req_skills.withIndex().associate { it.value to it.index }
        val n = people.size
        val personMasks = IntArray(n)
        for (i in 0 until n) {
            var mask = 0
            for (skill in people[i]) mask = mask or (1 shl skillId[skill]!!)
            personMasks[i] = mask
        }
        val target = (1 shl req_skills.size) - 1
        val teamMask = IntArray(1 shl req_skills.size)
        val teamSize = IntArray(1 shl req_skills.size) { Int.MAX_VALUE }
        teamSize[0] = 0
        for (state in 0..target) {
            if (teamSize[state] == Int.MAX_VALUE) continue
            for (i in 0 until n) {
                val next = state or personMasks[i]
                if (teamSize[next] > teamSize[state] + 1) {
                    teamSize[next] = teamSize[state] + 1
                    teamMask[next] = teamMask[state] or (1 shl i)
                }
            }
        }
        val team = mutableListOf<Int>()
        for (i in 0 until n) {
            if ((teamMask[target] shr i) and 1 == 1) team.add(i)
        }
        return team.toIntArray()
    }
}
