// LeetCode 1950 - Maximum of Minimum Values in All Subarrays
// https://leetcode.com/problems/maximum-of-minimum-values-in-all-subarrays/

class Solution {
    func findMaximums(_ nums: [Int]) -> [Int] {
        let n = nums.count
        var left = Array(repeating: -1, count: n)
        var right = Array(repeating: n, count: n)
        var stack: [Int] = []
        for i in 0..<n {
            while !stack.isEmpty && nums[stack.last!] >= nums[i] { stack.removeLast() }
            left[i] = stack.last ?? -1
            stack.append(i)
        }
        stack = []
        for i in stride(from: n - 1, through: 0, by: -1) {
            while !stack.isEmpty && nums[stack.last!] >= nums[i] { stack.removeLast() }
            right[i] = stack.last ?? n
            stack.append(i)
        }
        var ans = Array(repeating: 0, count: n)
        for i in 0..<n {
            let length = right[i] - left[i] - 1
            ans[length - 1] = max(ans[length - 1], nums[i])
        }
        for i in stride(from: n - 2, through: 0, by: -1) {
            ans[i] = max(ans[i], ans[i + 1])
        }
        return ans
    }
}
