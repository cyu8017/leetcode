// LeetCode 2334 - Subarray With Elements Greater Than Varying Threshold
// https://leetcode.com/problems/subarray-with-elements-greater-than-varying-threshold/

class Solution {
    func validSubarraySize(_ nums: [Int], _ threshold: Int) -> Int {
        let n = nums.count
        var left = [Int](repeating: 0, count: n)
        var right = [Int](repeating: 0, count: n)
        var stack: [Int] = []
        for i in 0..<n {
            while let last = stack.last, nums[last] >= nums[i] { stack.removeLast() }
            left[i] = stack.last ?? -1
            stack.append(i)
        }
        stack.removeAll()
        for i in stride(from: n - 1, through: 0, by: -1) {
            while let last = stack.last, nums[last] >= nums[i] { stack.removeLast() }
            right[i] = stack.last ?? n
            stack.append(i)
        }
        for i in 0..<n {
            let k = right[i] - left[i] - 1
            if nums[i] > threshold / k { return k }
        }
        return -1
    }
}
