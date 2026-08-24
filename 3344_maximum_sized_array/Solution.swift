// LeetCode 3344 - Maximum Sized Array
// https://leetcode.com/problems/maximum-sized-array/

class Solution {
    func maxSizedArray(_ s: Int) -> Int {
        var lo = 1, hi = 2000
        while lo < hi {
            let mid = (lo + hi + 1) / 2
            if ok(mid, s) { lo = mid } else { hi = mid - 1 }
        }
        return lo
    }

    private func ok(_ n: Int, _ s: Int) -> Bool {
        var sum = 0
        for i in 0..<n {
            for j in 0..<n {
                let ij = i | j
                sum += ij * (n - 1) * n / 2
                if sum > s { return false }
            }
        }
        return sum <= s
    }
}
