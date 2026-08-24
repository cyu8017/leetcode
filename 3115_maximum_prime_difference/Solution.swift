// LeetCode 3115 - Maximum Prime Difference
// https://leetcode.com/problems/maximum-prime-difference/

class Solution {
    func maximumPrimeDifference(_ nums: [Int]) -> Int {
        func isPrime(_ n: Int) -> Bool {
            if n < 2 { return false }
            var i = 2
            while i <= n / i {
                if n % i == 0 { return false }
                i += 1
            }
            return true
        }
        var i = 0
        while true {
            if isPrime(nums[i]) {
                var j = nums.count - 1
                while true {
                    if isPrime(nums[j]) { return j - i }
                    j -= 1
                }
            }
            i += 1
        }
    }
}
