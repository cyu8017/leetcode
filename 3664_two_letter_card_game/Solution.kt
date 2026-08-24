// LeetCode 3664 - Two-Letter Card Game
// https://leetcode.com/problems/two-letter-card-game/

class Solution {
    private fun pairGroup(arr: IntArray): IntArray {
        var total = 0
        var mx = 0
        for (i in 0 until 26) {
            total += arr[i]
            mx = maxOf(mx, arr[i])
        }
        var pairs = total / 2
        if (total - mx < pairs) pairs = total - mx
        return intArrayOf(pairs, total - 2 * pairs)
    }

    fun score(cards: Array<String>, x: Char): Int {
        var xx = 0
        var left = IntArray(26)
        var right = IntArray(26)
        for (c in cards) {
            var a = c[0]
            var b = c[1]
            if (a == x && b == x) xx++
            else if (a == x) left[b - 'a']++
            else if (b == x) right[a - 'a']++
        }
        var lp = pairGroup(left)
        var rp = pairGroup(right)
        var ans = lp[0] + rp[0]
        var rem = lp[1] + rp[1]
        var use = minOf(xx, rem)
        ans += use
        xx -= use
        ans += xx / 2
        return ans
    }
}
