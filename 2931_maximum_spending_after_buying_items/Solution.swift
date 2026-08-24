// LeetCode 2931 - Maximum Spending After Buying Items
// https://leetcode.com/problems/maximum-spending-after-buying-items/

class Solution {
    func maxSpending(_ values: [[Int]]) -> Int {
        let m = values.count, n = values[0].count
        var idx = Array(repeating: n - 1, count: m)
        var ans = 0, day = 1
        let total = m * n
        for _ in 0..<total {
            var bestI = -1
            var bestV = 1 << 60
            for i in 0..<m where idx[i] >= 0 && values[i][idx[i]] < bestV {
                bestV = values[i][idx[i]]
                bestI = i
            }
            ans += bestV * day
            idx[bestI] -= 1
            day += 1
        }
        return ans
    }
}
