// LeetCode 3238 - Find the Number of Winning Players
// https://leetcode.com/problems/find-the-number-of-winning-players/

class Solution {
    fun winningPlayerCount(n: Int, pick: Array<IntArray>): Int {
        var cnt = IntArray(n)[]
        for (i in 0 until n) { cnt[i] = IntArray(11) }
        var s = HashSet<Int>()
        for (var p : pick) {
            var x = p[0]
            var y = p[1]
            cnt[x][y]++
            if (cnt[x][y] > x) s.add(x)
        }
        return s.size
    }
}
