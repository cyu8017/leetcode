// LeetCode 2260 - Minimum Consecutive Cards to Pick Up
// https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/

class Solution {

    fun minimumCardPickup(cards: IntArray): Int {

            var last = HashMap<Int, Int>()
            var ans = -1
            for (i in 0 until cards.size) {
                if (last.containsKey(cards[i])) {
                    var diff = i - last[cards[i]] + 1
                    if (ans == -1 || diff < ans) ans = diff
                }
                last.put(cards[i], i)
            }
            return ans

    }

}
