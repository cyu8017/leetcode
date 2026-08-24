// LeetCode 0649 - Dota2 Senate
// https://leetcode.com/problems/dota2-senate/


class Solution {
    fun predictPartyVictory(senate: String): String {
        val radiant = ArrayDeque<Int>()
        val dire = ArrayDeque<Int>()
        val n = senate.length
        for (i in senate.indices) {
            if (senate[i] == 'R') radiant.add(i) else dire.add(i)
        }
        while (radiant.isNotEmpty() && dire.isNotEmpty()) {
            val r = radiant.removeFirst()
            val d = dire.removeFirst()
            if (r < d) radiant.add(r + n) else dire.add(d + n)
        }
        return if (radiant.isNotEmpty()) "Radiant" else "Dire"
    }
}
