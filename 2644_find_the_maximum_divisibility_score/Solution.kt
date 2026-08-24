
// LeetCode 2644 - Find the Maximum Divisibility Score
// https://leetcode.com/problems/find-the-maximum-divisibility-score/

class Solution {
    fun maxDivScore(nums: IntArray, divisors: IntArray): Int {
        var best = divisors[0]
        var bestScore = -1
        for (d in divisors) {
            var score = 0
            for (x in nums) if (x % d == 0) score++
            if (score > bestScore || (score == bestScore && d < best)) {
                bestScore = score
                best = d
            }
        }
        return best
    }
}
