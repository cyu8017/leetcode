// LeetCode 3356 - Zero Array Transformation II
// https://leetcode.com/problems/zero-array-transformation-ii/

class Solution {
    func minZeroArray(_ nums: [Int], _ queries: [[Int]]) -> Int {
        let n = nums.count
        if ok(0, nums, queries, n) { return 0 }
        var lo = 1, hi = queries.count + 1
        while lo < hi {
            let mid = (lo + hi) / 2
            if mid <= queries.count && ok(mid, nums, queries, n) { hi = mid }
            else { lo = mid + 1 }
        }
        if lo > queries.count { return -1 }
        return lo
    }

    private func ok(_ k: Int, _ nums: [Int], _ queries: [[Int]], _ n: Int) -> Bool {
        var diff = Array(repeating: 0, count: n + 1)
        for i in 0..<k {
            let q = queries[i]
            diff[q[0]] += q[2]
            diff[q[1] + 1] -= q[2]
        }
        var cur = 0
        for i in 0..<n {
            cur += diff[i]
            if cur < nums[i] { return false }
        }
        return true
    }
}
