// LeetCode 3918 - Sum Of Primes Between Number And Its Reverse
// https://leetcode.com/problems/sum-of-primes-between-number-and-its-reverse/

class Solution {
    private static let isPrime: [Bool] = {
        var ip = [Bool](repeating: true, count: 1001)
        ip[0] = false
        ip[1] = false
        var i = 2
        while i * i <= 1000 {
            if ip[i] {
                var j = i * i
                while j <= 1000 {
                    ip[j] = false
                    j += i
                }
            }
            i += 1
        }
        return ip
    }()

    func sumOfPrimesInRange(_ n: Int) -> Int {
        var r = 0, x = n
        while x > 0 {
            r = r * 10 + x % 10
            x /= 10
        }
        let low = min(n, r), high = max(n, r)
        var ans = 0
        for x in low...high {
            if Solution.isPrime[x] { ans += x }
        }
        return ans
    }
}
