// LeetCode 3895 - Count Digit Appearances
// https://leetcode.com/problems/count-digit-appearances/

class Solution {
    func countDigitOccurrences(_ nums: [Int], _ digit: Int) -> Int {
        var ans = 0
        for num in nums {
            var x = num
            while x > 0 {
                if x % 10 == digit { ans += 1 }
                x /= 10
            }
        }
        return ans
    }
}
