// LeetCode 3036 - Number of Subarrays That Match a Pattern II
// https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-ii/

class Solution {
    func countMatchingSubarrays(_ nums: [Int], _ pattern: [Int]) -> Int {
        let N = pattern.count
        var ps = Array(repeating: 0, count: N + 1)
        ps[0] = -1
        ps[1] = 0
        var p = 0
        for i in 2...N {
            let x = pattern[i - 1]
            while p >= 0 && pattern[p] != x { p = ps[p] }
            p += 1
            ps[i] = p
        }
        var res = 0
        let M = nums.count
        p = 0
        for i in 1..<M {
            var t = nums[i] - nums[i - 1]
            if t > 0 { t = 1 }
            else if t < 0 { t = -1 }
            while p >= 0 && pattern[p] != t { p = ps[p] }
            p += 1
            if p == N {
                res += 1
                p = ps[p]
            }
        }
        return res
    }
}
