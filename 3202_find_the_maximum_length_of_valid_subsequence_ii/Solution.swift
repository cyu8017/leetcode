// LeetCode 3202 - Find the Maximum Length of Valid Subsequence II
// https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/

class Solution {
    func maximumLength(_ nums: [Int], _ k: Int) -> Int {
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
