// LeetCode 2347 - Best Poker Hand
// https://leetcode.com/problems/best-poker-hand/

class Solution {
    fun bestHand(ranks: IntArray, suits: CharArray): String {
        if (suits[0] == suits[1] && suits[1] == suits[2] && suits[2] == suits[3] && suits[3] == suits[4]) {
            return "Flush"
        }
        val cnt = HashMap<Int, Int>()
        var best = 0
        for (r in ranks) {
            val c = cnt.getOrDefault(r, 0) + 1
            cnt[r] = c
            best = maxOf(best, c)
        }
        if (best >= 3) return "Three of a Kind"
        if (best == 2) return "Pair"
        return "High Card"
    }
}
