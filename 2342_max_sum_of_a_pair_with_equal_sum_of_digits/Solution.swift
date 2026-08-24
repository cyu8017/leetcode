// LeetCode 2342 - Max Sum of a Pair With Equal Sum of Digits
// https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/

class Solution {
    func maximumSum(_ nums: [Int]) -> Int {
        func digitSum(_ x: Int) -> Int {
            var x = x, s = 0
            while x > 0 { s += x % 10; x /= 10 }
            return s
        }
        var best: [Int: Int] = [:]
        var ans = -1
        for x in nums {
            let ds = digitSum(x)
            if let prev = best[ds] {
                ans = max(ans, prev + x)
                if x > prev { best[ds] = x }
            } else {
                best[ds] = x
            }
        }
        return ans
    }
}
