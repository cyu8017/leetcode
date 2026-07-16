// LeetCode 0473 - Matchsticks to Square
// https://leetcode.com/problems/matchsticks-to-square/

class Solution {
    func makesquare(_ matchsticks: [Int]) -> Bool {
        if matchsticks.isEmpty { return false }
        let total = matchsticks.reduce(0, +)
        if total % 4 != 0 { return false }
        let side = total / 4
        let sorted = matchsticks.sorted(by: >)

        func dfs(_ index: Int, _ sides: inout [Int]) -> Bool {
            if index == sorted.count {
                return sides[0] == side && Set(sides).count == 1
            }
            let length = sorted[index]
            for sideIndex in 0..<4 {
                if sides[sideIndex] + length > side { continue }
                if sideIndex > 0 && sides[sideIndex] == sides[sideIndex - 1] { continue }
                sides[sideIndex] += length
                if dfs(index + 1, &sides) {
                    return true
                }
                sides[sideIndex] -= length
            }
            return false
        }

        return dfs(0, &[0, 0, 0, 0])
    }
}
