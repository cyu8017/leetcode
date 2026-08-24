// LeetCode 2012 - Sum of Beauty in the Array
// https://leetcode.com/problems/sum-of-beauty-in-the-array/

class Solution {
    func sumOfBeauties(_ nums: [Int]) -> Int {
        let n = nums.count
        var prefixMax = [Int](repeating: 0, count: n)
        var suffixMin = [Int](repeating: 0, count: n)
        prefixMax[0] = nums[0]
        for i in 1..<n { prefixMax[i] = max(prefixMax[i - 1], nums[i]) }
        suffixMin[n - 1] = nums[n - 1]
        for i in stride(from: n - 2, through: 0, by: -1) {
            suffixMin[i] = min(suffixMin[i + 1], nums[i])
        }
        var ans = 0
        for i in 1..<(n - 1) {
            if prefixMax[i - 1] < nums[i] && nums[i] < suffixMin[i + 1] { ans += 2 }
            else if nums[i - 1] < nums[i] && nums[i] < nums[i + 1] { ans += 1 }
        }
        return ans
    }
}
