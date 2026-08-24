// LeetCode 2312 - Selling Pieces of Wood
// https://leetcode.com/problems/selling-pieces-of-wood/

class Solution {
    func sellingWood(_ m: Int, _ n: Int, _ prices: [[Int]]) -> Int {
        var price = [[Int]](repeating: [Int](repeating: 0, count: n + 1), count: m + 1)
        var dp = price
        for p in prices { price[p[0]][p[1]] = p[2] }
        for h in 1...m {
            for w in 1...n {
                var best = price[h][w]
                if h > 1 {
                    for i in 1..<h { best = max(best, dp[i][w] + dp[h - i][w]) }
                }
                if w > 1 {
                    for j in 1..<w { best = max(best, dp[h][j] + dp[h][w - j]) }
                }
                dp[h][w] = best
            }
        }
        return dp[m][n]
    }
}
