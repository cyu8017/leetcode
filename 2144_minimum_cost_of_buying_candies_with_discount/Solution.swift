// LeetCode 2144 - Minimum Cost of Buying Candies With Discount
// https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/

class Solution {
    func minimumCost(_ cost: [Int]) -> Int {
        let arr = cost.sorted(by: >)
        var ans = 0
        for i in 0..<arr.count where i % 3 != 2 { ans += arr[i] }
        return ans
    }
}
