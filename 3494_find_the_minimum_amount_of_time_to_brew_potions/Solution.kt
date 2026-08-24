// LeetCode 3494 - Find the Minimum Amount of Time to Brew Potions
// https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/

class Solution {
    fun minTime(skill: IntArray, mana: IntArray): Long {
        val n = skill.size
        val m = mana.size
        val done = LongArray(n)
        for (j in 0 until m) {
            var t = 0L
            for (i in 0 until n) {
                if (done[i] > t) t = done[i]
                t += skill[i].toLong() * mana[j]
                done[i] = t
            }
            for (i in n - 2 downTo 0) {
                done[i] = done[i + 1] - skill[i + 1].toLong() * mana[j]
            }
        }
        return done[n - 1]
    }
}
