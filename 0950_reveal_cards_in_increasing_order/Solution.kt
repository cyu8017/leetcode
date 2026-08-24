// LeetCode 0950 - Reveal Cards In Increasing Order
// https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution {
    fun deckRevealedIncreasing(deck: IntArray): IntArray {
        deck.sort()
        val n = deck.size
        val idx = ArrayDeque<Int>()
        for (i in 0 until n) idx.addLast(i)
        val ans = IntArray(n)
        for (card in deck) {
            ans[idx.removeFirst()] = card
            if (idx.isNotEmpty()) idx.addLast(idx.removeFirst())
        }
        return ans
    }
}
