// LeetCode 3569 - Maximize Count of Distinct Primes After Split
// https://leetcode.com/problems/maximize-count-of-distinct-primes-after-split/

class Solution {
    func maximumCount(_ nums: [Int], _ queries: [[Int]]) -> [Int] {
        var nums = nums
        var mx = 0
        for v in nums { mx = max(mx, v) }
        for q in queries { mx = max(mx, q[1]) }
        var isP = Array(repeating: false, count: mx + 1)
        if mx >= 2 {
            for i in 2...mx { isP[i] = true }
            var i = 2
            while i * i <= mx {
                if isP[i] {
                    var j = i * i
                    while j <= mx { isP[j] = false; j += i }
                }
                i += 1
            }
        }
        var ans = Array(repeating: 0, count: queries.count)
        for qi in 0..<queries.count {
            nums[queries[qi][0]] = queries[qi][1]
            var best = 0
            var left = [Int: Int]()
            var right = [Int: Int]()
            for v in nums where v <= mx && isP[v] { right[v, default: 0] += 1 }
            if nums.count > 1 {
                for i in 0..<(nums.count - 1) {
                    let v = nums[i]
                    if v <= mx && isP[v] {
                        left[v, default: 0] += 1
                        let c = right[v]! - 1
                        if c == 0 { right[v] = nil } else { right[v] = c }
                    }
                    best = max(best, left.count + right.count)
                }
            }
            ans[qi] = best
        }
        return ans
    }
}
