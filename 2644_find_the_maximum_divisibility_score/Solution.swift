// LeetCode 2644 - Find the Maximum Divisibility Score
// https://leetcode.com/problems/find-the-maximum-divisibility-score/

class Solution {
    func maxDivScore(_ nums: [Int], _ divisors: [Int]) -> Int {
        var best = divisors[0]
        var bestScore = -1
        for d in divisors {
            var score = 0
            for x in nums where x % d == 0 { score += 1 }
            if score > bestScore || (score == bestScore && d < best) {
                bestScore = score
                best = d
            }
        }
        return best
    }
}
