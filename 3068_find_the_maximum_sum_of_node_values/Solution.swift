// LeetCode 3068 - Find the Maximum Sum of Node Values
// https://leetcode.com/problems/find-the-maximum-sum-of-node-values/

class Solution {
    func maximumValueSum(_ nums: [Int], _ k: Int, _ edges: [[Int]]) -> Int {
        var f0 = 0
        var f1 = Int.min / 4
        for x in nums {
            let nf0 = max(f0 + x, f1 + (x ^ k))
            let nf1 = max(f1 + x, f0 + (x ^ k))
            f0 = nf0
            f1 = nf1
        }
        return f0
    }
}
