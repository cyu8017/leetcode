// LeetCode 1891 - Cutting Ribbons
// https://leetcode.com/problems/cutting-ribbons/

class Solution {
    func maxLength(_ ribbons: [Int], _ k: Int) -> Int {
        func can(_ length: Int) -> Bool {
            ribbons.reduce(0) { $0 + $1 / length } >= k
        }

        var lo = 1
        var hi = ribbons.max() ?? 0
        while lo < hi {
            let mid = (lo + hi + 1) / 2
            if can(mid) {
                lo = mid
            } else {
                hi = mid - 1
            }
        }
        return can(lo) ? lo : 0
    }
}
