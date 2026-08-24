// LeetCode 2778 - Sum of Squares of Special Elements
// https://leetcode.com/problems/sum-of-squares-of-special-elements/

class Solution {
    func sumOfSquares(_ nums: [Int]) -> Int {
        let n = nums.count
        var ans = 0
        for i in 0..<n where n % (i + 1) == 0 { ans += nums[i] * nums[i] }
        return ans
    }
}
