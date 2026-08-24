// LeetCode 0793 - Preimage Size of Factorial Zeroes Function
// https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/

class Solution {
    func preimageSizeFZF(_ k: Int) -> Int {
        return Int(firstGe(k + 1) - firstGe(k))
    }

    private func zeros(_ n: Int) -> Int {
        var n = n, z = 0
        while n > 0 {
            n /= 5
            z += n
        }
        return z
    }

    private func firstGe(_ target: Int) -> Int {
        var lo = 0, hi = 5 * target + 5
        while lo < hi {
            let mid = (lo + hi) / 2
            if zeros(mid) >= target { hi = mid }
            else { lo = mid + 1 }
        }
        return lo
    }
}
