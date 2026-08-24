// LeetCode 3152 - Special Array II
// https://leetcode.com/problems/special-array-ii/

class Solution {
    func isArraySpecial(_ nums: [Int], _ queries: [[Int]]) -> [Bool] {
        let n = nums.count
        var d = Array(0..<n)
        for i in 1..<n {
            if nums[i] % 2 != nums[i - 1] % 2 { d[i] = d[i - 1] }
        }
        return queries.map { d[$0[1]] <= $0[0] }
    }
}
