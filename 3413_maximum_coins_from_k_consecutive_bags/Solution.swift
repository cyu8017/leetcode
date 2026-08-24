// LeetCode 3413 - Maximum Coins From K Consecutive Bags
// https://leetcode.com/problems/maximum-coins-from-k-consecutive-bags/

class Solution {
    func maximumCoins(_ coins: [[Int]], _ k: Int) -> Int {
        let coins = coins.sorted { $0[0] < $1[0] }
        var ans = 0
        let n = coins.count
        for i in 0..<n {
            var sum = 0
            let start = coins[i][0]
            let end = start + k - 1
            var j = i
            while j < n && coins[j][0] <= end {
                var l = coins[j][0], r = coins[j][1]
                if r > end { r = end }
                if l < start { l = start }
                if l <= r { sum += (r - l + 1) * coins[j][2] }
                j += 1
            }
            if sum > ans { ans = sum }
        }
        for i in 0..<n {
            var sum = 0
            let end = coins[i][1]
            let start = end - k + 1
            for j in 0...i {
                var l = coins[j][0], r = coins[j][1]
                if l < start { l = start }
                if r > end { r = end }
                if l <= r { sum += (r - l + 1) * coins[j][2] }
            }
            if sum > ans { ans = sum }
        }
        return ans
    }
}
