// LeetCode 3946 - Maximum Number of Items From Sale I
// https://leetcode.com/problems/maximum-number-of-items-from-sale-i/


class Solution {
    func maximumSaleItems(_ items: [[Int]], _ budget: Int) -> Int {
        var f = Array(repeating: 0, count: budget + 1)
        var mn = Int.max
        for item in items {
            let factor = item[0], price = item[1]
            mn = min(mn, price)
            var cnt = 0
            for jItem in items {
                if jItem[0] % factor == 0 { cnt += 1 }
            }
            if price <= budget {
                for j in stride(from: budget, through: price, by: -1) {
                    f[j] = max(f[j], f[j - price] + cnt)
                }
            }
        }
        var ans = 0
        for i in 0...budget {
            let extra = mn == 0 ? 0 : (budget - i) / mn
            ans = max(ans, f[i] + extra)
        }
        return ans
    }
}
