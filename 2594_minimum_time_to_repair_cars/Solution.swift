// LeetCode 2594 - Minimum Time to Repair Cars
// https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution {
    func repairCars(_ ranks: [Int], _ cars: Int) -> Int {
        let mn = ranks.min()!
        var lo = 1, hi = mn * cars * cars
        func ok(_ t: Int) -> Bool {
            var done = 0
            for r in ranks {
                var l = 0, h = cars
                while l < h {
                    let mid = (l + h + 1) / 2
                    if r * mid * mid <= t { l = mid } else { h = mid - 1 }
                }
                done += l
                if done >= cars { return true }
            }
            return done >= cars
        }
        while lo < hi {
            let mid = (lo + hi) / 2
            if ok(mid) { hi = mid } else { lo = mid + 1 }
        }
        return lo
    }
}
