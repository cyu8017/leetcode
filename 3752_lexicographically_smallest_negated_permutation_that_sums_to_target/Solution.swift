// LeetCode 3752 - Lexicographically Smallest Negated Permutation that Sums to Target
// https://leetcode.com/problems/lexicographically-smallest-negated-permutation-that-sums-to-target/

class Solution {
    func lexicographicallySmallest(_ n: Int, _ target: Int) -> [Int] {
        let total = n * (n + 1) / 2
        if target < -total || target > total || (total - target) % 2 != 0 { return [] }
        var remaining = (total - target) / 2
        var negative = [Bool](repeating: false, count: n + 1)
        for value in stride(from: n, through: 1, by: -1) {
            if value <= remaining {
                negative[value] = true
                remaining -= value
            }
        }
        var answer = [Int]()
        for value in stride(from: n, through: 1, by: -1) {
            if negative[value] { answer.append(-value) }
        }
        for value in 1...n {
            if !negative[value] { answer.append(value) }
        }
        return answer
    }
}
