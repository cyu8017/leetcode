// LeetCode 3660 - Jump Game IX
// https://leetcode.com/problems/jump-game-ix/

class Solution {
    func maxValue(_ nums: [Int]) -> [Int] {
        let n = nums.count
        var ans = Array(repeating: 0, count: n)
        var preMax = Array(repeating: 0, count: n)
        preMax[0] = nums[0]
        if n > 1 {
            for i in 1..<n { preMax[i] = max(preMax[i - 1], nums[i]) }
        }
        var sufMin = Int.max / 2
        for i in stride(from: n - 1, through: 0, by: -1) {
            if preMax[i] > sufMin { ans[i] = ans[i + 1] }
            else { ans[i] = preMax[i] }
            sufMin = min(sufMin, nums[i])
        }
        return ans
    }
}
