// LeetCode 2498 - Frog Jump II
// https://leetcode.com/problems/frog-jump-ii/

class Solution {
    func maxJump(_ stones: [Int]) -> Int {
        var ans = stones[1] - stones[0]
        for i in 2..<stones.count {
            ans = max(ans, stones[i] - stones[i - 2])
        }
        return ans
    }
}
