// LeetCode 1856 - Maximum Subarray Min-Product
// https://leetcode.com/problems/maximum-subarray-min-product/

class Solution {
    func maxSumMinProduct(_ nums: [Int]) -> Int {
        let mod = 1_000_000_007
        let n = nums.count
        var prefix = Array(repeating: Int64(0), count: n + 1)
        for i in 0..<n {
            prefix[i + 1] = prefix[i] + Int64(nums[i])
        }

        var leftBound = Array(repeating: -1, count: n)
        var stack: [Int] = []
        for i in 0..<n {
            while !stack.isEmpty && nums[stack.last!] >= nums[i] {
                stack.removeLast()
            }
            leftBound[i] = stack.isEmpty ? -1 : stack.last!
            stack.append(i)
        }

        var rightBound = Array(repeating: n, count: n)
        stack.removeAll()
        for i in stride(from: n - 1, through: 0, by: -1) {
            while !stack.isEmpty && nums[stack.last!] >= nums[i] {
                stack.removeLast()
            }
            rightBound[i] = stack.isEmpty ? n : stack.last!
            stack.append(i)
        }

        var best: Int64 = 0
        for i in 0..<n {
            let total = prefix[rightBound[i]] - prefix[leftBound[i] + 1]
            best = max(best, total * Int64(nums[i]))
        }

        return Int(best % Int64(mod))
    }
}
