// LeetCode 3605 - Minimum Stability Factor of Array
// https://leetcode.com/problems/minimum-stability-factor-of-array/

class Solution {
    func minStable(_ nums: [Int], _ maxC: Int) -> Int {
        let n = nums.count
        var lo = 0, hi = n
        while lo < hi {
            let mid = (lo + hi) / 2
            if ok(nums, maxC, mid) { hi = mid } else { lo = mid + 1 }
        }
        return lo
    }

    func ok(_ nums: [Int], _ maxC: Int, _ x: Int) -> Bool {
        let n = nums.count
        if x >= n { return true }
        var changes = 0, i = 0
        while i + x < n {
            var g = nums[i]
            for j in (i + 1)...(i + x) { g = gcd(g, nums[j]) }
            if g > 1 {
                changes += 1
                i += x + 1
            } else {
                i += 1
            }
        }
        return changes <= maxC
    }

    func gcd(_ a0: Int, _ b0: Int) -> Int {
        var a = a0, b = b0
        while b != 0 { let t = a % b; a = b; b = t }
        return a
    }
}
