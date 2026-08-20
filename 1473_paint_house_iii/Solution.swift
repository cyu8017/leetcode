// LeetCode 1473 - Paint House III
// https://leetcode.com/problems/paint-house-iii/

class Solution {
    func minCost(_ houses: [Int], _ cost: [[Int]], _ m: Int, _ n: Int, _ target: Int) -> Int {
        let inf = Int.max / 4
        var dp = [0: 0] // key = prev*100 + groups
        for (i, painted) in houses.enumerated() {
            var nxt = [Int: Int]()
            let colors = painted != 0 ? [painted] : Array(1...n)
            for (key, value) in dp {
                let prev = key / 100, groups = key % 100
                for color in colors {
                    let ng = groups + (color != prev ? 1 : 0)
                    if ng <= target {
                        let nv = value + (painted != 0 ? 0 : cost[i][color - 1])
                        let nk = color * 100 + ng
                        nxt[nk] = min(nxt[nk, default: inf], nv)
                    }
                }
            }
            dp = nxt
        }
        let ans = dp.filter { $0.key % 100 == target }.map { $0.value }.min() ?? inf
        return ans == inf ? -1 : ans
    }
}
