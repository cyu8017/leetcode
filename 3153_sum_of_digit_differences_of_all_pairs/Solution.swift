// LeetCode 3153 - Sum of Digit Differences of All Pairs
// https://leetcode.com/problems/sum-of-digit-differences-of-all-pairs/

class Solution {
    func sumDigitDifferences(_ nums: [Int]) -> Int {
        let n = nums.count
        var m = 0
        var t = nums[0]
        while t > 0 { m += 1; t /= 10 }
        var ans = 0
        var vals = nums
        for _ in 0..<m {
            var cnt = Array(repeating: 0, count: 10)
            for i in 0..<n {
                cnt[vals[i] % 10] += 1
                vals[i] /= 10
            }
            for v in cnt { ans += v * (n - v) }
        }
        return ans / 2
    }
}
