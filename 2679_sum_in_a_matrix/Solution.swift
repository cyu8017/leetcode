// LeetCode 2679 - Sum in a Matrix
// https://leetcode.com/problems/sum-in-a-matrix/

class Solution {
    func matrixSum(_ nums: [[Int]]) -> Int {
        var nums = nums
        for i in nums.indices { nums[i].sort() }
        var ans = 0
        let n = nums[0].count
        for j in 0..<n {
            var mx = 0
            for row in nums { mx = max(mx, row[j]) }
            ans += mx
        }
        return ans
    }
}
