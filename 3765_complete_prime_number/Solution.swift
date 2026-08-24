// LeetCode 3765 - Complete Prime Number
// https://leetcode.com/problems/complete-prime-number/

class Solution {
    private func isPrime(_ x: Int) -> Bool {
        if x < 2 { return false }
        var i = 2
        while i * i <= x {
            if x % i == 0 { return false }
            i += 1
        }
        return true
    }

    func completePrime(_ num: Int) -> Bool {
        let s = Array(String(num))
        var x = 0
        for c in s {
            x = x * 10 + Int(c.asciiValue! - 48)
            if !isPrime(x) { return false }
        }
        x = 0
        var p = 1
        for i in stride(from: s.count - 1, through: 0, by: -1) {
            x = p * Int(s[i].asciiValue! - 48) + x
            p *= 10
            if !isPrime(x) { return false }
        }
        return true
    }
}
