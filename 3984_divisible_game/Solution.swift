// LeetCode 3984 - Divisible Game
// https://leetcode.com/problems/divisible-game/


class Solution {
    func divisibleGame(_ nums: [Int]) -> Int {
        var candidates = Set<Int>()
        candidates.insert(2)
        for value in nums {
            var divisor = 2
            while divisor * divisor <= value {
                if value % divisor == 0 {
                    candidates.insert(divisor)
                    candidates.insert(value / divisor)
                }
                divisor += 1
            }
            if value > 1 { candidates.insert(value) }
        }
        var bestScore = -(Int.max / 4)
        var bestK = 0
        for k in candidates {
            var ending = 0, score = 0
            for i in 0..<nums.count {
                let value = nums[i]
                var contribution = -value
                if value % k == 0 { contribution = value }
                if i == 0 || ending + contribution < contribution { ending = contribution }
                else { ending += contribution }
                if i == 0 || ending > score { score = ending }
            }
            if score > bestScore || (score == bestScore && k < bestK) {
                bestScore = score
                bestK = k
            }
        }
        let mod = 1_000_000_007
        var answer = (bestScore % mod) * bestK % mod
        if answer < 0 { answer += mod }
        return answer
    }
}
