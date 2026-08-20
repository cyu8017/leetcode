// LeetCode 1340 - Jump Game V
// https://leetcode.com/problems/jump-game-v/

class Solution {
    func maxJumps(_ arr: [Int], _ d: Int) -> Int {
        var dp = Array(repeating: 1, count: arr.count)
        let order = arr.enumerated().map { ($0.element, $0.offset) }.sorted { $0.0 < $1.0 }
        for (_, i) in order {
            for step in [-1, 1] {
                var j = i + step
                while j >= 0 && j < arr.count && abs(j - i) <= d && arr[j] < arr[i] {
                    dp[i] = max(dp[i], 1 + dp[j])
                    j += step
                }
            }
        }
        return dp.max() ?? 1
    }
}
