// LeetCode 2431 - Maximize Total Tastiness of Purchased Fruits
// https://leetcode.com/problems/maximize-total-tastiness-of-purchased-fruits/

class Solution {
    func maxTastiness(_ price: [Int], _ tastiness: [Int], _ maxAmount: Int, _ maxCoupons: Int) -> Int {
        let n = price.count
        let neg = Int.min / 4
        var dp = [[Int]](repeating: [Int](repeating: neg, count: maxCoupons + 1), count: maxAmount + 1)
        dp[0][0] = 0
        for i in 0..<n {
            let p = price[i], t = tastiness[i]
            for a in stride(from: maxAmount, through: 0, by: -1) {
                for c in stride(from: maxCoupons, through: 0, by: -1) {
                    if dp[a][c] < 0 { continue }
                    if a + p <= maxAmount {
                        dp[a + p][c] = max(dp[a + p][c], dp[a][c] + t)
                    }
                    if c + 1 <= maxCoupons && a + p / 2 <= maxAmount {
                        dp[a + p / 2][c + 1] = max(dp[a + p / 2][c + 1], dp[a][c] + t)
                    }
                }
            }
        }
        var ans = 0
        for a in 0...maxAmount {
            for c in 0...maxCoupons { ans = max(ans, dp[a][c]) }
        }
        return ans
    }
}
