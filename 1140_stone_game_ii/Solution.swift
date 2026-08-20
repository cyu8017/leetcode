// LeetCode 1140 - Stone Game II
// https://leetcode.com/problems/stone-game-ii/

class Solution {
    func stoneGameII(_ piles: [Int]) -> Int {
        let n = piles.count
        var suffix = [Int](repeating: 0, count: n + 1)
        for i in stride(from: n - 1, through: 0, by: -1) {
            suffix[i] = suffix[i + 1] + piles[i]
        }
        var memo = [[Int?]](repeating: [Int?](repeating: nil, count: n + 1), count: n)
        func dfs(_ i: Int, _ m: Int) -> Int {
            if i >= n { return 0 }
            if i + m >= n { return suffix[i] }
            if let v = memo[i][m] { return v }
            var best = Int.max
            for x in 1...min(2 * m, n - i) {
                best = min(best, dfs(i + x, max(x, m)))
            }
            let ans = suffix[i] - best
            memo[i][m] = ans
            return ans
        }
        return dfs(0, 1)
    }
}
