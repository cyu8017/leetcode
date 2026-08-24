// LeetCode 2614 - Prime In Diagonal
// https://leetcode.com/problems/prime-in-diagonal/

class Solution {
    func diagonalPrime(_ nums: [[Int]]) -> Int {
        func isPrime(_ x: Int) -> Bool {
            if x < 2 { return false }
            var i = 2
            while i * i <= x {
                if x % i == 0 { return false }
                i += 1
            }
            return true
        }
        let n = nums.count
        var best = 0
        for i in 0..<n {
            let a = nums[i][i], b = nums[i][n - 1 - i]
            if isPrime(a) { best = max(best, a) }
            if isPrime(b) { best = max(best, b) }
        }
        return best
    }
}
