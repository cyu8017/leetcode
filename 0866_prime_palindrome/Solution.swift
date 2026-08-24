// LeetCode 0866 - Prime Palindrome
// https://leetcode.com/problems/prime-palindrome/

class Solution {
    func primePalindrome(_ n: Int) -> Int {
        if n <= 2 { return 2 }
        if n <= 3 { return 3 }
        if n <= 5 { return 5 }
        if n <= 7 { return 7 }
        if n <= 11 { return 11 }
        func isPrime(_ x: Int) -> Bool {
            if x < 2 { return false }
            if x % 2 == 0 { return x == 2 }
            var d = 3
            while d * d <= x {
                if x % d == 0 { return false }
                d += 2
            }
            return true
        }
        for length in 1...5 {
            let start = Int(pow(10.0, Double(length - 1)))
            let end = Int(pow(10.0, Double(length)))
            for root in start..<end {
                let s = Array(String(root))
                var pal = s
                for i in stride(from: s.count - 2, through: 0, by: -1) { pal.append(s[i]) }
                let val = Int(String(pal))!
                if val >= n && isPrime(val) { return val }
            }
        }
        return 0
    }
}
