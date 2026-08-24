// LeetCode 3824 - Minimum K To Reduce Array Within Limit
// https://leetcode.com/problems/minimum-k-to-reduce-array-within-limit/

class Solution {
    func minimumK(_ nums: [Int]) -> Int {
        var lo = 1, hi = 100000
        while lo < hi {
            let mid = (lo + hi) / 2
            if check(nums, mid) { hi = mid }
            else { lo = mid + 1 }
        }
        return lo
    }

    private func check(_ nums: [Int], _ k: Int) -> Bool {
        var t = 0
        for x in nums { t += (x + k - 1) / k }
        return t <= k * k
    }
}
