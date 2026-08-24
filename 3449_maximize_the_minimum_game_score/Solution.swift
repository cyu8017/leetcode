// LeetCode 3449 - Maximize the Minimum Game Score
// https://leetcode.com/problems/maximize-the-minimum-game-score/

class Solution {
    func maxScore(_ points: [Int], _ m: Int) -> Int {
        var lo = 0, hi = Int(1e18)
        while lo < hi {
            let mid = (lo + hi + 1) / 2
            if ok(points, m, mid) { lo = mid }
            else { hi = mid - 1 }
        }
        return lo
    }

    private func ok(_ points: [Int], _ m: Int, _ mid: Int) -> Bool {
        var need = 0
        var extra = 0
        for p in points {
            let req = (mid + p - 1) / p
            if req > extra {
                let visits = req - extra
                need += 2 * visits - 1
                extra = visits - 1
            } else {
                need += 1
                extra = 0
            }
            if need > m { return false }
        }
        return need <= m
    }
}
