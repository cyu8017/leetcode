// LeetCode 2731 - Movement of Robots
// https://leetcode.com/problems/movement-of-robots/

class Solution {
    fun sumDistance(nums: IntArray, s: String, d: Int): Int {
        val MOD = 1_000_000_007
        val n = nums.size
        val pos = LongArray(n)
        for (i in 0 until n) {
            pos[i] = nums[i].toLong() + if (s[i] == 'R') d else -d
        }
        pos.sort()
        var ans = 0L
        var pref = 0L
        for (i in 0 until n) {
            ans = (ans + pos[i] * i - pref) % MOD
            pref += pos[i]
        }
        return ((ans % MOD + MOD) % MOD).toInt()
    }
}
