// LeetCode 0441 - Arranging Coins
// https://leetcode.com/problems/arranging-coins/

class Solution {
    func arrangeCoins(_ n: Int) -> Int {
        var low = 0
        var high = n
        while low <= high {
            let mid = low + (high - low) / 2
            if mid * (mid + 1) / 2 <= n {
                low = mid + 1
            } else {
                high = mid - 1
            }
        }
        return high
    }
}
