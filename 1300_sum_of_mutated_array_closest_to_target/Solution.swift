// LeetCode 1300 - Sum of Mutated Array Closest to Target
// https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/

class Solution {
    func findBestValue(_ arr: [Int], _ target: Int) -> Int {
        var lo = 0, hi = arr.max() ?? 0
        while lo < hi {
            let mid = (lo + hi) / 2
            let sum = arr.reduce(0) { $0 + min($1, mid) }
            if sum < target { lo = mid + 1 } else { hi = mid }
        }
        let before = arr.reduce(0) { $0 + min($1, lo - 1) }
        let after = arr.reduce(0) { $0 + min($1, lo) }
        return target - before <= after - target ? lo - 1 : lo
    }
}
