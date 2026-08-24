// LeetCode 3591 - Check if Any Element Has Prime Frequency
// https://leetcode.com/problems/check-if-any-element-has-prime-frequency/

class Solution {
    func isPrime(_ x: Int) -> Bool {
        if x < 2 { return false }
        var i = 2
        while i * i <= x {
            if x % i == 0 { return false }
            i += 1
        }
        return true
    }

    func checkPrimeFrequency(_ nums: [Int]) -> Bool {
        var cnt = [Int: Int]()
        for x in nums { cnt[x, default: 0] += 1 }
        for v in cnt.values where isPrime(v) { return true }
        return false
    }
}
