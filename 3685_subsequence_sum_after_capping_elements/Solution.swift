// LeetCode 3685 - Subsequence Sum After Capping Elements
// https://leetcode.com/problems/subsequence-sum-after-capping-elements/

class Solution {
    func subsequenceSumAfterCapping(_ nums: [Int], _ k: Int) -> [Bool] {
        let n = nums.count
        let sorted = nums.sorted()
        var ans = Array(repeating: false, count: n)
        var reach = Array(repeating: false, count: k + 1)
        reach[0] = true
        var idx = 0
        for x in 1...n {
            while idx < n && sorted[idx] <= x {
                let v = sorted[idx]
                if v <= k {
                    for s in stride(from: k, through: v, by: -1) {
                        if reach[s - v] { reach[s] = true }
                    }
                }
                idx += 1
            }
            var tmp = reach
            let rem = n - idx
            for s in 0...k {
                if !reach[s] { continue }
                var t = 1
                while t <= rem && s + t * x <= k {
                    tmp[s + t * x] = true
                    t += 1
                }
            }
            ans[x - 1] = tmp[k]
        }
        return ans
    }
}
