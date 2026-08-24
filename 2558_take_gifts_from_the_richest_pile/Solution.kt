// LeetCode 2558 - Take Gifts From the Richest Pile
// https://leetcode.com/problems/take-gifts-from-the-richest-pile/

class Solution {
    fun pickGifts(gifts: IntArray, k: Int): Long {
        var h = PriorityQueue((a, b) -> (b).compareTo(a))
        for (g in gifts) { h.offer(g) }
        for (i in 0 until k) {
            var x = h.poll()
            h.offer(kotlin.math.sqrt(x))
        }
        var ans = 0
        while (!h.isEmpty()) ans += h.poll()
        return ans
    }
}
