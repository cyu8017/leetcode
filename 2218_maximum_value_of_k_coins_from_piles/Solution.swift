// LeetCode 2218 - Maximum Value of K Coins From Piles
// https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/

class Solution {
    func maxValueOfCoins(_ piles: [[Int]], _ k: Int) -> Int {
        var dp = [Int](repeating: 0, count: k + 1)
        for pile in piles {
            var ndp = dp
            var sum = 0
            let takeMax = min(pile.count, k)
            for take in 1...takeMax {
                sum += pile[take - 1]
                for j in take...k {
                    ndp[j] = max(ndp[j], dp[j - take] + sum)
                }
            }
            dp = ndp
        }
        return dp[k]
    }
}
