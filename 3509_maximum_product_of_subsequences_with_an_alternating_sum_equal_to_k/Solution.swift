// LeetCode 3509 - Maximum Product of Subsequences With an Alternating Sum Equal to K
// https://leetcode.com/problems/maximum-product-of-subsequences-with-an-alternating-sum-equal-to-k/

class Solution {
    let MIN = -5000
    var memo = [String: Int]()
    var nums = [Int]()
    var limit = 0

    func dp(_ i: Int, _ product: Int, _ state: Int, _ kk: Int) -> Int {
        if i == nums.count {
            if kk == 0 && state != 0 && product <= limit { return product }
            return MIN
        }
        let key = "\(i),\(product),\(state),\(kk)"
        if let v = memo[key] { return v }
        var res = dp(i + 1, product, state, kk)
        if state == 0 { res = max(res, dp(i + 1, nums[i], 1, kk - nums[i])) }
        if state == 1 {
            var np = product * nums[i]
            if np > limit + 1 { np = limit + 1 }
            res = max(res, dp(i + 1, np, 2, kk + nums[i]))
        }
        if state == 2 {
            var np = product * nums[i]
            if np > limit + 1 { np = limit + 1 }
            res = max(res, dp(i + 1, np, 1, kk - nums[i]))
        }
        memo[key] = res
        return res
    }

    func maxProduct(_ nums_: [Int], _ k: Int, _ limit_: Int) -> Int {
        nums = nums_
        limit = limit_
        memo = [:]
        var sumAll = 0
        for v in nums { sumAll += v }
        if abs(k) > sumAll { return -1 }
        let ans = dp(0, 1, 0, k)
        return ans == MIN ? -1 : ans
    }
}
