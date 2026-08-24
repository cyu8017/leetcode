// LeetCode 2081 - Sum of k-Mirror Numbers
// https://leetcode.com/problems/sum-of-k-mirror-numbers/

class Solution {
    func kMirror(_ k: Int, _ n: Int) -> Int {
        var ans = 0, count = 0, length = 1
        while count < n {
            var start = 1
            for _ in 1..<(length + 1) / 2 { start *= 10 }
            let end = start * 10
            var half = start
            while half < end && count < n {
                var pal = half
                if length % 2 == 0 {
                    var x = half
                    while x > 0 { pal = pal * 10 + x % 10; x /= 10 }
                } else {
                    var x = half / 10
                    while x > 0 { pal = pal * 10 + x % 10; x /= 10 }
                }
                if isPalBase(pal, k) {
                    ans += pal
                    count += 1
                }
                half += 1
            }
            length += 1
        }
        return ans
    }

    private func isPalBase(_ x: Int, _ bas: Int) -> Bool {
        var x = x
        var digits = [Int]()
        while x > 0 {
            digits.append(x % bas)
            x /= bas
        }
        var l = 0, r = digits.count - 1
        while l < r {
            if digits[l] != digits[r] { return false }
            l += 1; r -= 1
        }
        return true
    }
}
