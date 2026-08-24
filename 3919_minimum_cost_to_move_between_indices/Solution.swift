// LeetCode 3919 - Minimum Cost To Move Between Indices
// https://leetcode.com/problems/minimum-cost-to-move-between-indices/

class Solution {
    func minCost(_ nums: [Int], _ queries: [[Int]]) -> [Int] {
        let n = nums.count
        var s1 = [Int](repeating: 0, count: n)
        var s2 = [Int](repeating: 0, count: n)
        if n > 1 {
            for i in 1..<n {
                var c1 = 1
                if i > 1 && nums[i - 1] - nums[i - 2] <= nums[i] - nums[i - 1] { c1 = nums[i] - nums[i - 1] }
                var c2 = 1
                if i < n - 1 && nums[i] - nums[i - 1] > nums[i + 1] - nums[i] { c2 = nums[i] - nums[i - 1] }
                s1[i] = s1[i - 1] + c1
                s2[i] = s2[i - 1] + c2
            }
        }
        var ans = [Int](repeating: 0, count: queries.count)
        for i in 0..<queries.count {
            let l = queries[i][0], r = queries[i][1]
            ans[i] = (l < r) ? (s1[r] - s1[l]) : (s2[l] - s2[r])
        }
        return ans
    }
}
