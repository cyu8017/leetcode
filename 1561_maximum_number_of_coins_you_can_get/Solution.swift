// LeetCode 1561 - Maximum Number of Coins You Can Get
// https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution {
    func maxCoins(_ piles: [Int]) -> Int {
        let sorted = piles.sorted()
        var ans = 0
        var i = sorted.count / 3
        while i < sorted.count {
            ans += sorted[i]
            i += 2
        }
        return ans
    }
}
