// LeetCode 3300 - Minimum Element After Replacement With Digit Sum
// https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/

class Solution {
    func minElement(_ nums: [Int]) -> Int {
        var ans = 1_000_000_000
        for num in nums {
            var x = num, s = 0
            while x > 0 { s += x % 10; x /= 10 }
            if s < ans { ans = s }
        }
        return ans
    }
}
