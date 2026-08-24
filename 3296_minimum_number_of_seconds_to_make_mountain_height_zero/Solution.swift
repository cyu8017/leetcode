// LeetCode 3296 - Minimum Number of Seconds to Make Mountain Height Zero
// https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/

class Solution {
    func minNumberOfSeconds(_ mountainHeight: Int, _ workerTimes: [Int]) -> Int {
        var lo = 0, hi = Int(1e18)
        while lo < hi {
            let mid = (lo + hi) / 2
            if ok(mid, mountainHeight, workerTimes) { hi = mid }
            else { lo = mid + 1 }
        }
        return lo
    }

    private func ok(_ t: Int, _ mountainHeight: Int, _ workerTimes: [Int]) -> Bool {
        var total = 0
        for w in workerTimes {
            var l = 0, h = mountainHeight
            while l < h {
                let mid = (l + h + 1) / 2
                if w * mid * (mid + 1) / 2 <= t { l = mid }
                else { h = mid - 1 }
            }
            total += l
            if total >= mountainHeight { return true }
        }
        return total >= mountainHeight
    }
}
