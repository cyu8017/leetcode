// LeetCode 2496 - Maximum Value of a String in an Array
// https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/

class Solution {
    func maximumValue(_ strs: [String]) -> Int {
        var ans = 0
        for s in strs {
            var allDigit = true
            var val = 0
            for c in s {
                guard let d = c.wholeNumberValue else {
                    allDigit = false
                    break
                }
                val = val * 10 + d
            }
            if !allDigit { val = s.count }
            ans = max(ans, val)
        }
        return ans
    }
}
