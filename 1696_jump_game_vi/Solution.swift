// LeetCode 1696 - Jump Game VI
// https://leetcode.com/problems/jump-game-vi/

class Solution {
    func maxResult(_ nums: [Int], _ k: Int) -> Int {
        var q = [(0, nums[0])]
        for i in 1..<nums.count {
            while q[0].0 < i - k { q.removeFirst() }
            let score = nums[i] + q[0].1
            while !q.isEmpty && q.last!.1 <= score { q.removeLast() }
            q.append((i, score))
        }
        return q.last!.1
    }
}
