// LeetCode 3410 - Maximize Subarray Sum After Removing All Occurrences of One Element
// https://leetcode.com/problems/maximize-subarray-sum-after-removing-all-occurrences-of-one-element/

class Solution {
    func maxSubarraySum(_ nums: [Int]) -> Int {
        var ans = kadane(nums)
        var uniq = Set<Int>()
        for x in nums where x < 0 { uniq.insert(x) }
        for v in uniq {
            let b = nums.filter { $0 != v }
            if b.isEmpty { continue }
            let cand = kadane(b)
            if cand > ans { ans = cand }
        }
        return ans
    }

    private func kadane(_ a: [Int]) -> Int {
        var best = -(1 << 62), cur = 0
        for x in a {
            cur += x
            if cur > best { best = cur }
            if cur < 0 { cur = 0 }
        }
        var allNeg = true
        var mx = a[0]
        for x in a {
            if x > mx { mx = x }
            if x >= 0 { allNeg = false }
        }
        if allNeg { return mx }
        return best
    }
}
