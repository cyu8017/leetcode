// LeetCode 3176 - Find the Maximum Length of a Good Subsequence I
// https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-i/

class Solution {
    func maximumLength(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var f = Array(repeating: Array(repeating: 0, count: k + 1), count: n)
        var ans = 0
        for i in 0..<n {
            for h in 0...k {
                for j in 0..<i {
                    if nums[i] == nums[j] { f[i][h] = max(f[i][h], f[j][h]) }
                    else if h > 0 { f[i][h] = max(f[i][h], f[j][h - 1]) }
                }
                f[i][h] += 1
            }
            ans = max(ans, f[i][k])
        }
        return ans
    }
}
