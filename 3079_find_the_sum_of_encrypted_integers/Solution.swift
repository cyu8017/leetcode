// LeetCode 3079 - Find the Sum of Encrypted Integers
// https://leetcode.com/problems/find-the-sum-of-encrypted-integers/

class Solution {
    func sumOfEncryptedInt(_ nums: [Int]) -> Int {
        var ans = 0
        for x in nums { ans += encrypt(x) }
        return ans
    }

    private func encrypt(_ x: Int) -> Int {
        var val = x, mx = 0, p = 0
        while val > 0 {
            mx = max(mx, val % 10)
            p = p * 10 + 1
            val /= 10
        }
        return mx * p
    }
}
