// LeetCode 0948 - Bag of Tokens
// https://leetcode.com/problems/bag-of-tokens/

class Solution {
    fun bagOfTokensScore(tokens: IntArray, power: Int): Int {
        tokens.sort()
        var i = 0
        var j = tokens.size - 1
        var score = 0
        var ans = 0
        while (i <= j) {
            if (power >= tokens[i]) {
                power -= tokens[i++]
                score++
                ans = maxOf(ans, score)
            } else if (score > 0) {
                power += tokens[j--]
                score--
            } else break
        }
        return ans
    }
}
