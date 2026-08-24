// LeetCode 0679 - 24 Game
// https://leetcode.com/problems/24-game/

class Solution {
    private let eps = 1e-6

    func judgePoint24(_ cards: [Int]) -> Bool {
        dfs(cards.map { Double($0) })
    }

    private func dfs(_ nums: [Double]) -> Bool {
        if nums.count == 1 { return abs(nums[0] - 24.0) < eps }
        for i in 0..<nums.count {
            for j in 0..<nums.count where i != j {
                var rest = [Double]()
                for k in 0..<nums.count where k != i && k != j { rest.append(nums[k]) }
                let a = nums[i], b = nums[j]
                var candidates = [a + b, a - b, a * b]
                if abs(b) > eps { candidates.append(a / b) }
                for value in candidates {
                    rest.append(value)
                    if dfs(rest) { return true }
                    rest.removeLast()
                }
            }
        }
        return false
    }
}
