// LeetCode 2815 - Max Pair Sum in an Array
// https://leetcode.com/problems/max-pair-sum-in-an-array/

class Solution {
    func maxSum(_ nums: [Int]) -> Int {
        var best: [Int: Int] = [:]
        var ans = -1
        for v in nums {
            var x = v, md = 0
            while x > 0 { md = max(md, x % 10); x /= 10 }
            if let prev = best[md] {
                ans = max(ans, prev + v)
                best[md] = max(prev, v)
            } else {
                best[md] = v
            }
        }
        return ans
    }
}
