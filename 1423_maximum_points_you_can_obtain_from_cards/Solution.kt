// LeetCode 1423 - Maximum Points You Can Obtain from Cards
// https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

class Solution {
    fun maxScore(cardPoints: IntArray, k: Int): Int {
        val n = cardPoints.size
        if (k == n) return cardPoints.sum()
        val window = n - k
        var current = 0
        for (i in 0 until window) current += cardPoints[i]
        var smallest = current
        for (i in window until n) {
            current += cardPoints[i] - cardPoints[i - window]
            smallest = minOf(smallest, current)
        }
        var total = 0
        for (v in cardPoints) total += v
        return total - smallest
    }
}
