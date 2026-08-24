// LeetCode 3281 - Maximize Score of Numbers in Ranges
// https://leetcode.com/problems/maximize-score-of-numbers-in-ranges/

class Solution {
    func maxPossibleScore(_ start: [Int], _ d: Int) -> Int {
        let a = start.sorted()
        let n = a.count
        var lo = 0, hi = a[n - 1] + d - a[0] + 1
        while lo < hi {
            let mid = (lo + hi + 1) / 2
            if ok(a, d, mid) { lo = mid }
            else { hi = mid - 1 }
        }
        return lo
    }

    private func ok(_ start: [Int], _ d: Int, _ mid: Int) -> Bool {
        var prev = start[0]
        for i in 1..<start.count {
            let need = prev + mid
            let cur = start[i]
            if need > cur + d { return false }
            prev = need > cur ? need : cur
        }
        return true
    }
}
