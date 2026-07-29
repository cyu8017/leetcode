// LeetCode 1004 - Max Consecutive Ones III
// https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution {
    func longestOnes(_ nums: [Int], _ k: Int) -> Int {
        var left = 0, zeros = 0, ans = 0
        for right in 0..<nums.count {
            if nums[right] == 0 { zeros += 1 }
            while zeros > k {
                if nums[left] == 0 { zeros -= 1 }
                left += 1
            }
            ans = max(ans, right - left + 1)
        }
        return ans
    }
}
