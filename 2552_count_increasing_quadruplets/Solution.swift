// LeetCode 2552 - Count Increasing Quadruplets
// https://leetcode.com/problems/count-increasing-quadruplets/

class Solution {
    func countQuadruplets(_ nums: [Int]) -> Int {
        let n = nums.count
        var ans = 0
        var great = [Int](repeating: 0, count: n)
        for j in 0..<n {
            for i in 0..<j {
                if nums[i] < nums[j] { ans += great[i] }
                else if nums[i] > nums[j] { great[i] += 1 }
            }
        }
        return ans
    }
}
