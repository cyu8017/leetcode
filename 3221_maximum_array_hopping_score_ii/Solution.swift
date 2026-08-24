// LeetCode 3221 - Maximum Array Hopping Score II
// https://leetcode.com/problems/maximum-array-hopping-score-ii/

class Solution {
    func maxScore(_ nums: [Int]) -> Int {
        var stk: [Int] = []
        for i in 0..<nums.count {
            while !stk.isEmpty && nums[stk.last!] <= nums[i] { stk.removeLast() }
            stk.append(i)
        }
        var ans = 0, cur = 0
        for j in stk {
            ans += (j - cur) * nums[j]
            cur = j
        }
        return ans
    }
}
