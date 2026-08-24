// LeetCode 2155 - All Divisions With the Highest Score of a Binary Array
// https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/

class Solution {
    func maxScoreIndices(_ nums: [Int]) -> [Int] {
        let n = nums.count
        let total1 = nums.reduce(0, +)
        var best = total1, left0 = 0, right1 = total1
        var ans = [0]
        for i in 0..<n {
            if nums[i] == 0 { left0 += 1 }
            else { right1 -= 1 }
            let score = left0 + right1
            if score > best { best = score; ans = [i + 1] }
            else if score == best { ans.append(i + 1) }
        }
        return ans
    }
}
