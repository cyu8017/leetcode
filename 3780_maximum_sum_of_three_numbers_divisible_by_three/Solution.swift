// LeetCode 3780 - Maximum Sum Of Three Numbers Divisible By Three
// https://leetcode.com/problems/maximum-sum-of-three-numbers-divisible-by-three/

class Solution {
    func maximumSum(_ nums: [Int]) -> Int {
        let a = nums.sorted()
        var g = [[Int]](repeating: [], count: 3)
        for x in a { g[x % 3].append(x) }
        var ans = 0
        for aa in 0..<3 {
            if !g[aa].isEmpty {
                let x = g[aa].removeLast()
                for b in 0..<3 {
                    if !g[b].isEmpty {
                        let y = g[b].removeLast()
                        let c = (3 - (aa + b) % 3) % 3
                        if !g[c].isEmpty {
                            let z = g[c][g[c].count - 1]
                            ans = max(ans, x + y + z)
                        }
                        g[b].append(y)
                    }
                }
                g[aa].append(x)
            }
        }
        return ans
    }
}
