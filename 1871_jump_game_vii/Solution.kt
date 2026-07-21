// LeetCode 1871 - Jump Game VII
// https://leetcode.com/problems/jump-game-vii/

class Solution {
    fun canReach(s: String, minJump: Int, maxJump: Int): Boolean {
        val n = s.length
        val reachable = BooleanArray(n)
        reachable[0] = true
        val prefix = IntArray(n + 1)
        for (i in 0 until n) {
            if (i > 0 && s[i] == '0') {
                val left = maxOf(0, i - maxJump)
                val right = i - minJump
                if (right >= left && prefix[right + 1] - prefix[left] > 0) {
                    reachable[i] = true
                }
            }
            prefix[i + 1] = prefix[i] + if (reachable[i]) 1 else 0
        }
        return reachable[n - 1]
    }
}
