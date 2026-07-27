// LeetCode 1664 - Ways to Make a Fair Array
// https://leetcode.com/problems/ways-to-make-a-fair-array/

class Solution {
    func waysToMakeFair(_ nums: [Int]) -> Int {
        var te = 0, to = 0
        for i in 0..<nums.count {
            if i % 2 == 1 { to += nums[i] } else { te += nums[i] }
        }
        var le = 0, lo = 0, ans = 0
        for i in 0..<nums.count {
            let x = nums[i]
            if i % 2 == 1 { to -= x } else { te -= x }
            if le + to == lo + te { ans += 1 }
            if i % 2 == 1 { lo += x } else { le += x }
        }
        return ans
    }
}
