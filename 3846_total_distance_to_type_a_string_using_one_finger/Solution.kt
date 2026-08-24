// LeetCode 3846 - Total Distance To Type A String Using One Finger
// https://leetcode.com/problems/total-distance-to-type-a-string-using-one-finger/

class Solution {
    private val POS: MutableMap<Char, IntArray> = buildPos()

    private fun buildPos(): MutableMap<Char, IntArray> {
        var pos = HashMap<Char, IntArray>()
        var keys = { "qwertyuiop", "asdfghjkl", "zxcvbnm" }
        for (i in 0 until 3) {
            for (j in 0 until keys[i].length) {
                pos[keys[i][j]] = intArrayOf( i, j )
            }
        }
        return pos
    }

    fun totalDistance(s: String): Int {
        var pre = 'a'
        var ans = 0
        for (cur in s.toCharArray()) {
            var p1 = POS[pre]
            var p2 = POS[cur]
            ans += kotlin.math.abs(p1[0] - p2[0]) + kotlin.math.abs(p1[1] - p2[1])
            pre = cur
        }
        return ans
    }
}
