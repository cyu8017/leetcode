// LeetCode 3755 - Find Maximum Balanced Xor Subarray Length
// https://leetcode.com/problems/find-maximum-balanced-xor-subarray-length/

class Solution {
    func maxBalancedSubarray(_ nums: [Int]) -> Int {
        var d = [Int: Int]()
        var a = 0, b = nums.count, ans = 0
        d[b] = -1
        for i in 0..<nums.count {
            a ^= nums[i]
            if nums[i] % 2 == 0 { b += 1 } else { b -= 1 }
            let key = (a << 32) | (b & 0xffffffff)
            if let prev = d[key] { ans = max(ans, i - prev) }
            else { d[key] = i }
        }
        return ans
    }
}
