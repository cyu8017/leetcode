// LeetCode 1815 - Maximum Number of Groups Getting Fresh Donuts
// https://leetcode.com/problems/maximum-number-of-groups-getting-fresh-donuts/

class Solution {
    func maxHappyGroups(_ batchSize: Int, _ groups: [Int]) -> Int {
        var count = Array(repeating: 0, count: batchSize)
        for size in groups {
            count[size % batchSize] += 1
        }
        var memo = [String: Int]()

        func dfs(_ remainder: Int, _ state: inout [Int]) -> Int {
            let key = "\(remainder)|\(state.map(String.init).joined(separator: ","))"
            if let cached = memo[key] { return cached }
            var best = 0
            for mod in 1..<batchSize where state[mod] > 0 {
                state[mod] -= 1
                best = max(best, dfs((remainder + mod) % batchSize, &state))
                state[mod] += 1
            }
            if remainder == 0 { best += 1 }
            memo[key] = best
            return best
        }

        var state = count
        var ans = dfs(0, &state)
        if count[0] > 0 {
            ans += count[0] - 1
        }
        return ans
    }
}
