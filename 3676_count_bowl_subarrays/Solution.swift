// LeetCode 3676 - Count Bowl Subarrays
// https://leetcode.com/problems/count-bowl-subarrays/

class Solution {
    func bowlSubarrays(_ nums: [Int]) -> Int {
        let n = nums.count
        var ans = 0
        var ngr = Array(repeating: -1, count: n)
        var ngl = Array(repeating: -1, count: n)
        var stack = [Int]()
        for i in stride(from: n - 1, through: 0, by: -1) {
            while !stack.isEmpty && nums[stack.last!] < nums[i] { stack.removeLast() }
            if !stack.isEmpty { ngr[i] = stack.last! }
            stack.append(i)
        }
        stack = []
        for i in 0..<n {
            while !stack.isEmpty && nums[stack.last!] < nums[i] { stack.removeLast() }
            if !stack.isEmpty { ngl[i] = stack.last! }
            stack.append(i)
        }
        for i in 0..<n {
            if ngr[i] != -1 && ngr[i] - i >= 2 { ans += 1 }
            if ngl[i] != -1 && i - ngl[i] >= 2 { ans += 1 }
        }
        return ans
    }
}
