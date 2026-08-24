// LeetCode 3984 - Divisible Game
// https://leetcode.com/problems/divisible-game/

class Solution {
    fun divisibleGame(nums: IntArray): Int {
        var candidates = HashSet<Int>()
        candidates.add(2)
        for (value in nums) {
            var divisor = 2
            while (divisor * divisor <= value) {
                if (value % divisor != 0) continue
                candidates.add(divisor)
                candidates.add(value / divisor)
                divisor++
            }
            if (value > 1) candidates.add(value)
        }
        var bestScore = -(1L  shl  62)
        var bestK = 0
        for (k in candidates) {
            var ending = 0
            var score = 0
            for (i in 0 until nums.size) {
                var value = nums[i]
                var contribution = -(value)
                if (value % k == 0) contribution = value
                if (i == 0 || ending + contribution < contribution) ending = contribution
                else ending += contribution
                if (i == 0 || ending > score) score = ending
            }
            if (score > bestScore || (score == bestScore && k < bestK)) {
                bestScore = score
                bestK = k
            }
        }
        val mod = 1000000007L
        var answer = (bestScore % mod) * bestK % mod
        if (answer < 0) answer += mod
        return answer
    }
}
