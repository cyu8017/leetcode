// LeetCode 2860 - Happy Students
// https://leetcode.com/problems/happy-students/

class Solution {
    func countWays(_ nums: [Int]) -> Int {
        let nums = nums.sorted()
        let n = nums.count
        var ans = 0
        if nums[0] > 0 { ans += 1 }
        for i in 0..<n {
            let selected = i + 1
            if selected > nums[i] && (i == n - 1 || selected < nums[i + 1]) {
                ans += 1
            }
        }
        return ans
    }
}
