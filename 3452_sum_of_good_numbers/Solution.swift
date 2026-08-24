// LeetCode 3452 - Sum of Good Numbers
// https://leetcode.com/problems/sum-of-good-numbers/

class Solution {
    func sumOfGoodNumbers(_ nums: [Int], _ k: Int) -> Int {
        var ans = 0
        let n = nums.count
        for i in 0..<n {
            var good = true
            if i - k >= 0 && nums[i] <= nums[i - k] { good = false }
            if i + k < n && nums[i] <= nums[i + k] { good = false }
            if good { ans += nums[i] }
        }
        return ans
    }
}
