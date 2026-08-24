// LeetCode 3018 - Maximum Number of Removal Queries That Can Be Processed I
// https://leetcode.com/problems/maximum-number-of-removal-queries-that-can-be-processed-i/

class Solution {
    func maximumProcessableQueries(_ nums: [Int], _ queries: [Int]) -> Int {
        let n = nums.count
        var f = Array(repeating: Array(repeating: 0, count: n), count: n)
        let m = queries.count
        for i in 0..<n {
            for j in stride(from: n - 1, through: i, by: -1) {
                if i > 0 {
                    let t = f[i - 1][j] < m && nums[i - 1] >= queries[f[i - 1][j]] ? 1 : 0
                    f[i][j] = max(f[i][j], f[i - 1][j] + t)
                }
                if j + 1 < n {
                    let t = f[i][j + 1] < m && nums[j + 1] >= queries[f[i][j + 1]] ? 1 : 0
                    f[i][j] = max(f[i][j], f[i][j + 1] + t)
                }
                if f[i][j] == m { return m }
            }
        }
        var ans = 0
        for i in 0..<n {
            let t = f[i][i] < m && nums[i] >= queries[f[i][i]] ? 1 : 0
            ans = max(ans, f[i][i] + t)
        }
        return ans
    }
}
