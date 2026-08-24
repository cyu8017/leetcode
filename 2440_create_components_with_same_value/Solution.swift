// LeetCode 2440 - Create Components With Same Value
// https://leetcode.com/problems/create-components-with-same-value/

class Solution {
    func componentValue(_ nums: [Int], _ edges: [[Int]]) -> Int {
        let n = nums.count
        let total = nums.reduce(0, +)
        var g = [[Int]](repeating: [], count: n)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        }
        func dfs(_ u: Int, _ p: Int, _ target: Int) -> Int {
            var sum = nums[u]
            for v in g[u] where v != p {
                let sub = dfs(v, u, target)
                if sub < 0 { return -1 }
                sum += sub
            }
            if sum > target { return -1 }
            if sum == target { return 0 }
            return sum
        }
        for parts in stride(from: n, through: 1, by: -1) {
            if total % parts != 0 { continue }
            let target = total / parts
            if dfs(0, -1, target) == 0 { return parts - 1 }
        }
        return 0
    }
}
