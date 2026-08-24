// LeetCode 3201 - Find the Maximum Length of Valid Subsequence I
// https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/

class Solution {
    func maximumLength(_ nums: [Int]) -> Int {
        let k = 2
        var f = Array(repeating: Array(repeating: 0, count: k), count: k)
        var ans = 0
        for raw in nums {
            let x = raw % k
            for j in 0..<k {
                let y = (j - x + k) % k
                f[x][y] = f[y][x] + 1
                ans = max(ans, f[x][y])
            }
        }
        return ans
    }
}
