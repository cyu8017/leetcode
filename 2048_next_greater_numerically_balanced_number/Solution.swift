// LeetCode 2048 - Next Greater Numerically Balanced Number
// https://leetcode.com/problems/next-greater-numerically-balanced-number/

class Solution {
    func nextBeautifulNumber(_ n: Int) -> Int {
        var x = n + 1
        while true {
            if balanced(x) { return x }
            x += 1
        }
    }

    private func balanced(_ x: Int) -> Bool {
        var x = x
        var cnt = [Int](repeating: 0, count: 10)
        while x > 0 {
            cnt[x % 10] += 1
            x /= 10
        }
        for d in 0..<10 where cnt[d] != 0 && cnt[d] != d { return false }
        return true
    }
}
