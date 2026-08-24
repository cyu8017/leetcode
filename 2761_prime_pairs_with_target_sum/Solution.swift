// LeetCode 2761 - Prime Pairs With Target Sum
// https://leetcode.com/problems/prime-pairs-with-target-sum/

class Solution {
    func findPrimePairs(_ n: Int) -> [[Int]] {
        if n < 2 { return [] }
        var isPrime = Array(repeating: false, count: n + 1)
        if n >= 2 { for i in 2...n { isPrime[i] = true } }
        var i = 2
        while i * i <= n {
            if isPrime[i] {
                var j = i * i
                while j <= n { isPrime[j] = false; j += i }
            }
            i += 1
        }
        var ans: [[Int]] = []
        if n >= 4 {
            for x in 2...(n / 2) {
                let y = n - x
                if isPrime[x] && isPrime[y] { ans.append([x, y]) }
            }
        }
        return ans
    }
}
