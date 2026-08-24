// LeetCode 2604 - Minimum Time to Eat All Grains
// https://leetcode.com/problems/minimum-time-to-eat-all-grains/

class Solution {
    func minimumTime(_ hens: [Int], _ grains: [Int]) -> Int {
        let hens = hens.sorted()
        let grains = grains.sorted()
        func ok(_ t: Int) -> Bool {
            var j = 0
            for h in hens {
                if j >= grains.count { return true }
                if grains[j] >= h {
                    while j < grains.count && grains[j] - h <= t { j += 1 }
                } else {
                    if h - grains[j] > t { return false }
                    let left = h - grains[j]
                    let maxRight1 = t - 2 * left
                    let maxRight2 = (t - left) / 2
                    var reach = h
                    if maxRight1 > maxRight2 {
                        if maxRight1 > 0 { reach = h + maxRight1 }
                    } else {
                        if maxRight2 > 0 { reach = h + maxRight2 }
                    }
                    while j < grains.count && grains[j] <= reach { j += 1 }
                }
            }
            return j >= grains.count
        }
        var lo = 0, hi = 2_000_000_000
        while lo < hi {
            let mid = lo + (hi - lo) / 2
            if ok(mid) { hi = mid } else { lo = mid + 1 }
        }
        return lo
    }
}
