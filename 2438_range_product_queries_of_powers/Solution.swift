// LeetCode 2438 - Range Product Queries of Powers
// https://leetcode.com/problems/range-product-queries-of-powers/

class Solution {
    func productQueries(_ n: Int, _ queries: [[Int]]) -> [Int] {
        let mod = 1_000_000_007
        var powers = [Int]()
        var n = n
        var bit = 0
        var x = n
        while x > 0 {
            if x & 1 != 0 { powers.append(1 << bit) }
            x >>= 1
            bit += 1
        }
        var ans = [Int](repeating: 0, count: queries.count)
        for i in 0..<queries.count {
            var prod = 1
            for j in queries[i][0]...queries[i][1] {
                prod = prod * powers[j] % mod
            }
            ans[i] = prod
        }
        return ans
    }
}
