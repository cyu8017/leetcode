// LeetCode 2819 - Minimum Relative Loss After Buying Chocolates
// https://leetcode.com/problems/minimum-relative-loss-after-buying-chocolates/

class Solution {
    func minimumRelativeLosses(_ prices: [Int], _ queries: [[Int]]) -> [Int] {
        let prices = prices.sorted()
        let n = prices.count
        return queries.map { q in
            let kk = q[0], m = q[1]
            var losses = prices.map { $0 <= kk ? $0 : 2 * kk - $0 }
            losses.sort()
            return losses.prefix(m).reduce(0, +)
        }
    }
}
