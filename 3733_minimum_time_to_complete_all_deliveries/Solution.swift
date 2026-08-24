// LeetCode 3733 - Minimum Time To Complete All Deliveries
// https://leetcode.com/problems/minimum-time-to-complete-all-deliveries/

class Solution {
    func minimumTime(_ d: [Int], _ r: [Int]) -> Int {
        var lo = 1, hi = Int(8e18)
        while lo < hi {
            let mid = lo + (hi - lo) / 2
            if ok(mid, d, r) { hi = mid }
            else { lo = mid + 1 }
        }
        return lo
    }

    private func ok(_ T: Int, _ d: [Int], _ r: [Int]) -> Bool {
        let w0 = T - T / r[0]
        let w1 = T - T / r[1]
        return w0 + w1 >= d[0] + d[1]
    }
}
