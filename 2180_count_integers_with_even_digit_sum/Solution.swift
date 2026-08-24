// LeetCode 2180 - Count Integers With Even Digit Sum
// https://leetcode.com/problems/count-integers-with-even-digit-sum/

class Solution {
    func countEven(_ num: Int) -> Int {
        var ans = 0
        for x in 1...num {
            var s = 0, y = x
            while y > 0 { s += y % 10; y /= 10 }
            if s % 2 == 0 { ans += 1 }
        }
        return ans
    }
}
