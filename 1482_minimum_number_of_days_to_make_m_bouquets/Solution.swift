// LeetCode 1482 - Minimum Number of Days to Make m Bouquets
// https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

class Solution {
    func minDays(_ bloomDay: [Int], _ m: Int, _ k: Int) -> Int {
        if m * k > bloomDay.count { return -1 }
        func possible(_ day: Int) -> Bool {
            var bouquets = 0, run = 0
            for x in bloomDay {
                run = x <= day ? run + 1 : 0
                if run == k { bouquets += 1; run = 0 }
            }
            return bouquets >= m
        }
        var lo = bloomDay.min()!, hi = bloomDay.max()!
        while lo < hi {
            let mid = (lo + hi) / 2
            if possible(mid) { hi = mid } else { lo = mid + 1 }
        }
        return lo
    }
}
