// LeetCode 3489 - Zero Array Transformation IV
// https://leetcode.com/problems/zero-array-transformation-iv/

class Solution {
    func minZeroArray(_ nums: [Int], _ queries: [[Int]]) -> Int {
        if ok(nums, queries, 0) { return 0 }
        var lo = 1, hi = queries.count + 1
        while lo < hi {
            let mid = (lo + hi) / 2
            if mid <= queries.count && ok(nums, queries, mid) { hi = mid }
            else { lo = mid + 1 }
        }
        return lo > queries.count ? -1 : lo
    }

    private func canSubsetSum(_ vals: [Int], _ target: Int) -> Bool {
        if target == 0 { return true }
        var dp = Array(repeating: false, count: target + 1)
        dp[0] = true
        for v in vals {
            for s in stride(from: target, through: v, by: -1) where dp[s - v] { dp[s] = true }
        }
        return dp[target]
    }

    private func ok(_ nums: [Int], _ queries: [[Int]], _ k: Int) -> Bool {
        for i in 0..<nums.count {
            if nums[i] == 0 { continue }
            var vals = [Int]()
            for q in 0..<k {
                if queries[q][0] <= i && i <= queries[q][1] { vals.append(queries[q][2]) }
            }
            if !canSubsetSum(vals, nums[i]) { return false }
        }
        return true
    }
}
