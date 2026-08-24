// LeetCode 2231 - Largest Number After Digit Swaps by Parity
// https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/

class Solution {
    func largestInteger(_ num: Int) -> Int {
        var digits: [Int] = []
        var x = num
        if x == 0 { digits = [0] }
        while x > 0 {
            digits.insert(x % 10, at: 0)
            x /= 10
        }
        var even = digits.filter { $0 % 2 == 0 }.sorted(by: >)
        var odd = digits.filter { $0 % 2 != 0 }.sorted(by: >)
        var ei = 0, oi = 0, ans = 0
        for d in digits {
            if d % 2 == 0 {
                ans = ans * 10 + even[ei]; ei += 1
            } else {
                ans = ans * 10 + odd[oi]; oi += 1
            }
        }
        return ans
    }
}
