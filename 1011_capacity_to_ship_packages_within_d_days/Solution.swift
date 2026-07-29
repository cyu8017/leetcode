// LeetCode 1011 - Capacity To Ship Packages Within D Days
// https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution {
    func shipWithinDays(_ weights: [Int], _ days: Int) -> Int {
        var lo = weights.max()!
        var hi = weights.reduce(0, +)
        func can(_ cap: Int) -> Bool {
            var need = 1, cur = 0
            for w in weights {
                if cur + w > cap {
                    need += 1
                    cur = 0
                }
                cur += w
            }
            return need <= days
        }
        while lo < hi {
            let mid = (lo + hi) / 2
            if can(mid) { hi = mid } else { lo = mid + 1 }
        }
        return lo
    }
}
