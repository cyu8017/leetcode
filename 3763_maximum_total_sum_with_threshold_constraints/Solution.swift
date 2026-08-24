// LeetCode 3763 - Maximum Total Sum With Threshold Constraints
// https://leetcode.com/problems/maximum-total-sum-with-threshold-constraints/

class Solution {
    func maxSum(_ nums: [Int], _ threshold: [Int]) -> Int {
        let n = nums.count
        var idx = Array(0..<n)
        idx.sort { threshold[$0] < threshold[$1] }
        var tree = [Int]()
        var ans = 0
        var i = 0
        var step = 1
        while true {
            while i < n && threshold[idx[i]] <= step {
                tree.append(nums[idx[i]])
                i += 1
            }
            tree.sort(by: >)
            if tree.isEmpty { break }
            ans += tree.removeFirst()
            step += 1
        }
        return ans
    }
}
