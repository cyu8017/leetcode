// LeetCode 3139 - Minimum Cost to Equalize Array
// https://leetcode.com/problems/minimum-cost-to-equalize-array/

class Solution {
    func minCostToEqualizeArray(_ nums: [Int], _ cost1: Int, _ cost2: Int) -> Int {
        let MOD = 1_000_000_007
        let n = nums.count
        let minNum = nums.min()!
        let maxNum = nums.max()!
        let sum = nums.reduce(0, +)
        if cost1 * 2 <= cost2 || n < 3 {
            let totalGap = maxNum * n - sum
            return cost1 * totalGap % MOD
        }
        var ans = Int.max
        for target in maxNum..<(2 * maxNum) {
            let maxGap = target - minNum
            let totalGap = target * n - sum
            var pairs = totalGap / 2
            let alt = totalGap - maxGap
            if alt < pairs { pairs = alt }
            let cost = cost1 * (totalGap - 2 * pairs) + cost2 * pairs
            ans = min(ans, cost)
        }
        return ans % MOD
    }
}
