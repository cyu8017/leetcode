// LeetCode 1814 - Count Nice Pairs in an Array
// https://leetcode.com/problems/count-nice-pairs-in-an-array/

class Solution {
    func countNicePairs(_ nums: [Int]) -> Int {
        let mod = 1_000_000_007
        var freq = [Int: Int]()
        var ans = 0
        for num in nums {
            let diff = num - rev(num)
            ans = (ans + (freq[diff] ?? 0)) % mod
            freq[diff, default: 0] += 1
        }
        return ans
    }

    private func rev(_ x: Int) -> Int {
        var n = x
        var r = 0
        while n > 0 {
            r = r * 10 + n % 10
            n /= 10
        }
        return r
    }
}
