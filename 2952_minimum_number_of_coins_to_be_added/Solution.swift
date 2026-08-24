// LeetCode 2952 - Minimum Number of Coins to be Added
// https://leetcode.com/problems/minimum-number-of-coins-to-be-added/

class Solution {
    func minimumAddedCoins(_ coins: [Int], _ target: Int) -> Int {
        let coins = coins.sorted()
        var ans = 0, reach = 0, i = 0
        while reach < target {
            if i < coins.count && coins[i] <= reach + 1 {
                reach += coins[i]
                i += 1
            } else {
                reach += reach + 1
                ans += 1
            }
        }
        return ans
    }
}
