// LeetCode 2862 - Maximum Element-Sum of a Complete Subset of Indices
// https://leetcode.com/problems/maximum-element-sum-of-a-complete-subset-of-indices/

class Solution {
    func maximumSum(_ nums: [Int]) -> Int {
        let n = nums.count
        var groups: [Int: Int] = [:]
        var ans = 0
        for i in 1...n {
            let sf = squareFree(i)
            let sum = groups[sf, default: 0] + nums[i - 1]
            groups[sf] = sum
            ans = max(ans, sum)
        }
        return ans
    }

    private func squareFree(_ x0: Int) -> Int {
        var x = x0, res = 1
        var p = 2
        while p * p <= x {
            var cnt = 0
            while x % p == 0 {
                x /= p
                cnt += 1
            }
            if cnt % 2 == 1 { res *= p }
            p += 1
        }
        if x > 1 { res *= x }
        return res
    }
}
